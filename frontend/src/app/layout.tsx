import type { Metadata } from "next";
import "../index.css";

export const metadata: Metadata = {
  title: "AI Agency Factory Command Workspace",
  description: "Autonomous Engine Control Matrix",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased bg-slate-950 text-slate-100 font-sans">
        {children}
      </body>
    </html>
  );
}
