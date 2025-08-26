export async function fetchJSON<T>(path: string): Promise<T>{
  const url = process.env.NEXT_PUBLIC_BACKEND_URL || 'http://localhost:8000';
  const res = await fetch(`${url}${path}`, { cache: 'no-store' });
  if(!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}
