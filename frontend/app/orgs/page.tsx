import Header from "../components/Header";

export default function OrgsPage(){
  return (
    <div>
      <Header title="Organizations" subtitle="(Demo scope only)" />
      <p className="text-sm text-gray-600">This demo uses a single pre-seeded organization and dataset. Extend here for multi-tenant support.</p>
    </div>
  )
}
