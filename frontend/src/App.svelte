<script>
  import { onMount } from "svelte";

  let idNumber = "";
  let result = null;
  let loading = false;
  let errorKey = null;
  let lang = "ar";
  let theme = "light";

  onMount(() => {
    if (typeof window !== "undefined") {
      const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
      theme = mediaQuery.matches ? "dark" : "light";

      const handleChange = (e) => {
        theme = e.matches ? "dark" : "light";
      };
      mediaQuery.addEventListener("change", handleChange);

      return () => mediaQuery.removeEventListener("change", handleChange);
    }
  });

  const translations = {
    ar: {
      title: "التحقق من الهوية أو الإقامة",
      subtitle: "أدخل رقم الهوية المكون من 10 أرقام (يبدأ بـ 1 أو 2)",
      verify: "تحقق",
      verifying: "جاري التحقق...",
      errorLength: "يجب أن تكون الهوية مكونة من 10 أرقام.",
      errorServer: "حدث خطأ في الاتصال بالخادم",
      valid: "رقم الهوية صحيح",
      invalid: "رقم الهوية غير صحيح",
      langToggle: "English",
      themeToggle: "🌙",
    },
    en: {
      title: "ID Verification",
      subtitle: "Enter the 10-digit ID number (starts with 1 or 2)",
      verify: "Verify",
      verifying: "Verifying...",
      errorLength: "The ID must consist of 10 digits.",
      errorServer: "Error connecting to the server",
      valid: "Valid ID number",
      invalid: "Invalid ID number",
      langToggle: "العربية",
      themeToggle: "☀️",
    },
  };

  $: t = translations[lang];

  $: {
    if (typeof document !== "undefined") {
      document.documentElement.dir = lang === "ar" ? "rtl" : "ltr";
      document.documentElement.lang = lang;
      if (theme === "dark") {
        document.body.classList.add("dark");
      } else {
        document.body.classList.remove("dark");
      }
    }
  }

  function toggleLang() {
    lang = lang === "ar" ? "en" : "ar";
  }

  function toggleTheme() {
    theme = theme === "light" ? "dark" : "light";
  }

  async function checkID() {
    if (idNumber.length !== 10) {
      errorKey = "errorLength";
      result = null;
      return;
    }

    errorKey = null;
    loading = true;

    try {
      const apiUrl = import.meta.env.VITE_API_URL || "http://localhost:8000";
      const response = await fetch(`${apiUrl}/validate/${idNumber}`);

      if (!response.ok) {
        throw new Error("errorServer");
      }
      const data = await response.json();
      result = data.isValid;
    } catch (err) {
      errorKey = "errorServer";
      result = null;
    } finally {
      loading = false;
    }
  }

  function handleInput(event) {
    // تحويل الأرقام العربية إلى إنجليزية ثم السماح بالأرقام فقط
    let value = event.target.value.replace(/[٠-٩]/g, (d) =>
      "٠١٢٣٤٥٦٧٨٩".indexOf(d),
    );
    idNumber = value.replace(/\D/g, "").slice(0, 10);
    result = null;
    errorKey = null;
  }
</script>

<main class="container">
  <div class="top-nav">
    <button class="icon-btn" on:click={toggleTheme} aria-label="Toggle Theme">
      {t.themeToggle}
    </button>
    <button class="text-btn" on:click={toggleLang} aria-label="Toggle Language">
      {t.langToggle}
    </button>
  </div>
  <div class="card">
    <h2>{t.title}</h2>
    <p class="subtitle">{t.subtitle}</p>

    <div class="input-group">
      <input
        type="text"
        value={idNumber}
        on:input={handleInput}
        on:keydown={(e) =>
          e.key === "Enter" && idNumber.length === 10 && !loading
            ? checkID()
            : null}
        maxlength="10"
        inputmode="numeric"
      />
      <button on:click={checkID} disabled={loading || idNumber.length !== 10}>
        {loading ? t.verifying : t.verify}
      </button>
    </div>

    {#if errorKey}
      <p class="error">{t[errorKey]}</p>
    {/if}

    {#if result !== null}
      <div class="result {result ? 'valid' : 'invalid'}">
        <div class="icon">{result ? "✅" : "❌"}</div>
        <p>{result ? t.valid : t.invalid}</p>
      </div>
    {/if}
  </div>
</main>

<style>
  :global(:root) {
    --bg-color: #f4f7f6;
    --card-bg: white;
    --text-primary: #2c3e50;
    --text-secondary: #7f8c8d;
    --border-color: #e0e0e0;
    --input-focus: #3498db;
    --btn-bg: #3498db;
    --btn-hover: #2980b9;
    --btn-disabled: #bdc3c7;
    --btn-text: white;
    --error-color: #e74c3c;
    --valid-bg: #e8f8f5;
    --valid-text: #27ae60;
    --valid-border: #a3e4d7;
    --invalid-bg: #fdedec;
    --invalid-text: #c0392b;
    --invalid-border: #f5b7b1;
    --shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  }

  :global(body.dark) {
    --bg-color: #121212;
    --card-bg: #1e1e1e;
    --text-primary: #f4f7f6;
    --text-secondary: #a0a0a0;
    --border-color: #333333;
    --input-focus: #5dade2;
    --btn-bg: #2980b9;
    --btn-hover: #3498db;
    --btn-disabled: #555555;
    --btn-text: #f4f7f6;
    --error-color: #f1948a;
    --valid-bg: #0e3020;
    --valid-text: #48c9b0;
    --valid-border: #117a65;
    --invalid-bg: #3b1717;
    --invalid-text: #ec7063;
    --invalid-border: #922b21;
    --shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
  }

  :global(body) {
    font-family: "Tajawal", "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    background-color: var(--bg-color);
    color: var(--text-primary);
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    transition:
      background-color 0.3s,
      color 0.3s;
  }

  .container {
    width: 100%;
    max-width: 400px;
    padding: 20px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    gap: 15px;
  }

  .top-nav {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
    margin-bottom: 5px;
  }

  .icon-btn,
  .text-btn {
    background: var(--card-bg);
    color: var(--text-primary);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 8px 12px;
    cursor: pointer;
    font-weight: bold;
    font-size: 1rem;
    transition: all 0.3s;
    box-shadow: var(--shadow);
  }

  .icon-btn:hover,
  .text-btn:hover {
    border-color: var(--btn-bg);
  }

  .card {
    background: var(--card-bg);
    border-radius: 12px;
    padding: 30px;
    box-shadow: var(--shadow);
    text-align: center;
    color: var(--text-primary);
    transition:
      background-color 0.3s,
      box-shadow 0.3s;
  }

  h2 {
    color: var(--text-primary);
    margin-top: 0;
    margin-bottom: 10px;
    font-size: 1.5rem;
  }

  .subtitle {
    color: var(--text-secondary);
    font-size: 0.9rem;
    margin-bottom: 24px;
  }

  .input-group {
    display: flex;
    flex-direction: column;
    gap: 15px;
    margin-bottom: 20px;
  }

  input {
    box-sizing: border-box;
    width: 100%;
    padding: 15px;
    font-size: 1.1rem;
    border: 2px solid var(--border-color);
    border-radius: 8px;
    text-align: center;
    background-color: var(--bg-color);
    color: var(--text-primary);
    transition:
      border-color 0.3s,
      background-color 0.3s,
      color 0.3s;
    outline: none;
  }

  input:focus {
    border-color: var(--input-focus);
    background-color: var(--card-bg);
  }

  button:not(.icon-btn):not(.text-btn) {
    box-sizing: border-box;
    width: 100%;
    background-color: var(--btn-bg);
    color: var(--btn-text);
    border: none;
    padding: 15px;
    font-size: 1.1rem;
    border-radius: 8px;
    cursor: pointer;
    font-weight: bold;
    transition: background-color 0.3s;
  }

  button:hover:not(:disabled):not(.icon-btn):not(.text-btn) {
    background-color: var(--btn-hover);
  }

  button:disabled {
    background-color: var(--btn-disabled);
    color: var(--text-secondary);
    cursor: not-allowed;
  }

  .error {
    color: var(--error-color);
    font-size: 0.9rem;
    margin-top: -10px;
    margin-bottom: 15px;
  }

  .result {
    margin-top: 20px;
    padding: 15px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    font-weight: bold;
    font-size: 1.1rem;
    animation: fadeIn 0.3s ease;
  }

  .icon {
    font-size: 1.5rem;
  }

  .valid {
    background-color: var(--valid-bg);
    color: var(--valid-text);
    border: 1px solid var(--valid-border);
  }

  .invalid {
    background-color: var(--invalid-bg);
    color: var(--invalid-text);
    border: 1px solid var(--invalid-border);
  }

  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: translateY(-10px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
</style>
