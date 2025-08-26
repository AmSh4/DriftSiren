import Header from "../components/Header";
import Table from "../components/Table";

async function fetchMetrics(){
  const url = process.env.NEXT_PUBLIC_BACKEND_URL || 'http://localhost:8000';
  const res = await fetch(`${url}/metrics`, { cache: 'no-store' });
  return res.json();
}

export default async function MetricsPage(){
  const rows = await fetchMetrics();
  return (
    <div>
      <Header title="Metrics" />
      <Table columns={['id','dataset_id','psi','ks','chi2','created_at']} rows={rows} />
    </div>
  )
}
