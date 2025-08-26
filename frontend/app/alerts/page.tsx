import Header from "../components/Header";
import Table from "../components/Table";

async function fetchAlerts(){
  const url = process.env.NEXT_PUBLIC_BACKEND_URL || 'http://localhost:8000';
  const res = await fetch(`${url}/alerts`, { cache: 'no-store' });
  return res.json();
}

export default async function AlertsPage(){
  const rows = await fetchAlerts();
  return (
    <div>
      <Header title="Alerts" />
      <Table columns={['id','dataset_id','severity','message','created_at']} rows={rows} />
    </div>
  )
}
