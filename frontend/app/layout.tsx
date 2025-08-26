import "./globals.css";
import Link from "next/link";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <header className="border-b bg-white/70 dark:bg-gray-900/70 backdrop-blur">
          <div className="container py-4 flex items-center justify-between">
            <div className="flex items-center gap-3">
              <img src="/logo.svg" alt="logo" className="h-8 w-8" />
              <h1 className="text-xl font-bold">DriftSiren</h1>
            </div>
            <nav className="flex gap-4 text-sm">
              <Link href="/">Dashboard</Link>
              <Link href="/metrics">Metrics</Link>
              <Link href="/alerts">Alerts</Link>
              <Link href="/orgs">Orgs</Link>
            </nav>
          </div>
        </header>
        <main className="container py-6">{children}</main>
      </body>
    </html>
  );
}
