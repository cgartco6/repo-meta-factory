import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        slate: {
          950: "#020617",
          900: "#0f172a",
          800: "#1e293b",
          700: "#334155",
          500: "#64748b",
          400: "#94a3b8",
          100: "#f1f5f9",
        },
        blue: {
          500: "#3b82f6",
          600: "#2563eb",
        },
        emerald: {
          400: "#34d399",
          500: "#10b981",
        },
        rose: {
          400: "#f87171",
          500: "#ef4444",
        }
      },
      fontFamily: {
        sans: ["var(--font-geist-sans)", "Inter", "sans-serif"],
        mono: ["var(--font-geist-mono)", "Fira Code", "monospace"],
      },
    },
  },
  plugins: [],
};

export default config;
