'use client';
import Header from "./components/Header";
import Card from "./components/Card";
import Chart from "./components/Chart";
import StatusDot from "./components/StatusDot";
import { useEffect, useState } from "react";

type Metric = { id:number; psi:number; ks:number; chi2:number; created_at:string };
type Alert = { id:number; severity:string; message:string; created_at:string };

export default function Page(){
  const [metrics, setMetrics] = useState<Metric[]>([]);
  const [alerts, setAlerts] = useState<Alert[]>([]);
  const [wsOK, setWsOK] = useState(false);

  async function load(){
    const url = process.env.NEXT_PUBLIC_BACKEND_URL || 'http://localhost:8000';
    const ms = await fetch(`${url}/metrics`).then(r=>r.json());
    const al = await fetch(`${url}/alerts`).then(r=>r.json());
    setMetrics(ms); setAlerts(al);
  }

  useEffect(()=>{
    load();
    const base = process.env.NEXT_PUBLIC_BACKEND_WS || 'ws://localhost:8000';
    const ws = new WebSocket(`${base}/ws/alerts`);
    ws.onopen = ()=> setWsOK(true);
    ws.onclose = ()=> setWsOK(false);
    ws.onmessage = (ev)=>{
      try{
        const m = JSON.parse(ev.data);
        if(m.type === 'alert'){
          setAlerts(prev => [{ id:m.id, severity:'HIGH', message:`PSI=${m.psi.toFixed(3)}, KS=${m.ks.toFixed(3)}`, created_at:new Date().toISOString() }, ...prev]);
        }
      }catch{}
    };
    return ()=> ws.close();
  }, []);

  const chartData = metrics.slice(0,30).reverse().map(m => ({
    time: new Date(m.created_at).toLocaleTimeString(),
    psi: m.psi, ks: m.ks, chi2: m.chi2
  }));

  return (
    <div>
      <Header title="Overview" subtitle="Real-time drift & data quality monitoring" />
      <div className="grid md:grid-cols-2 gap-4">
        <Card title="Live Connection">
          <div className="flex items-center gap-2">
            <StatusDot ok={wsOK} /> <span>WebSocket {wsOK ? 'connected' : 'disconnected'}</span>
          </div>
        </Card>
        <Card title="Recent Alerts">
          <ul className="space-y-2 max-h-64 overflow-auto">
            {alerts.map(a => <li key={a.id} className="p-2 rounded-lg bg-red-50 dark:bg-red-900/20">{a.message}</li>)}
          </ul>
        </Card>
        <Card title="Drift Metrics (last 30)">
          <Chart data={chartData} />
        </Card>
        <Card title="How to generate data">
{`1) docker compose up
2) python agent/ds_agent/client.py --backend http://localhost:8000 --dataset 1 --random 1000`}
        </Card>
      </div>
    </div>
  )
}
