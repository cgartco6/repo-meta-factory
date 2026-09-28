'use client';

import React, { useState } from 'react';
import { useRouter } from 'next/navigation';

export default function ClientIntakePortal() {
  const router = useRouter();
  const [formData, setFormData] = useState({
    companyName: '',
    industry: '',
    targetAudience: '',
    tier: 'freemium'
  });
  const [loading, setLoading] = useState(false);

  const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_API_URL || 'http://127.0.0.1:8000';

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      // Connects directly with our live Neon/Supabase integrated FastAPI endpoint
      const response = await fetch(`${BACKEND_URL}/api/v1/agency/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          company_name: formData.companyName,
          industry: formData.industry,
          target_audience: formData.targetAudience,
          tier: formData.tier,
        }),
      });

      if (response.ok) {
        router.push('/dashboard');
      } else {
        alert('Database registration rejected by the API cluster.');
      }
    } catch (err) {
      console.error('Database connection exception:', err);
      // Fallback redirection to dashboard if the developer laptop local API is cycling
      router.push('/dashboard');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-950 p-4">
      <form onSubmit={handleSubmit} className="bg-slate-900 border border-slate-800 p-8 rounded-xl max-w-md w-full space-y-4 shadow-2xl">
        <div>
          <h2 className="text-2xl font-black text-white tracking-tight">AGENCY ONBOARDING INTAKE</h2>
          <p className="text-xs text-slate-400 mt-1">Initialize automated brand pipelines instantly.</p>
        </div>
        <div>
          <label className="block text-xs font-bold text-slate-400 mb-1">COMPANY NAME</label>
          <input required type="text" className="w-full bg-slate-950 border border-slate-800 rounded p-2 text-sm text-white focus:outline-none focus:border-slate-600" 
            onChange={e => setFormData({...formData, companyName: e.target.value})} />
        </div>
        <div>
          <label className="block text-xs font-bold text-slate-400 mb-1">INDUSTRY</label>
          <input required type="text" className="w-full bg-slate-950 border border-slate-800 rounded p-2 text-sm text-white focus:outline-none focus:border-slate-600" 
            onChange={e => setFormData({...formData, industry: e.target.value})} />
        </div>
        <div>
          <label className="block text-xs font-bold text-slate-400 mb-1">TARGET AUDIENCE</label>
          <input required type="text" className="w-full bg-slate-950 border border-slate-800 rounded p-2 text-sm text-white focus:outline-none focus:border-slate-600" 
            onChange={e => setFormData({...formData, targetAudience: e.target.value})} />
        </div>
        <div>
          <label className="block text-xs font-bold text-slate-400 mb-1">TIER SUBSCRIPTION SELECTION</label>
          <select className="w-full bg-slate-950 border border-slate-800 rounded p-2 text-sm text-white focus:outline-none focus:border-slate-600"
            onChange={e => setFormData({...formData, tier: e.target.value})}>
            <option value="free">Free Tier</option>
            <option value="freemium">Freemium Tier</option>
            <option value="premium">Premium Engine</option>
          </select>
        </div>
        <button type="submit" disabled={loading} className="w-full bg-blue-600 hover:bg-blue-500 disabled:bg-slate-800 disabled:text-slate-500 py-2.5 rounded font-bold text-sm text-white transition-all cursor-pointer">
          {loading ? 'Processing Infrastructure Allocation...' : 'Initialize Factory Build Swarm ❯'}
        </button>
      </form>
    </div>
  );
}
