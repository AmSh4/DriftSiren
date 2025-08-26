'use client';
export function alertsSocket(): WebSocket {
  const base = process.env.NEXT_PUBLIC_BACKEND_WS || 'ws://localhost:8000';
  return new WebSocket(`${base}/ws/alerts`);
}
