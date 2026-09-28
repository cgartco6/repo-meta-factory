'use client';

import React, { useState, useEffect } from 'react';

interface ModuleState {
  friendly_name: string;
  status: string;
  progress: number;
  test_score: number;
  last_error: string | null;
  files: string[];
}

export default function FactoryCommandCenter() {
  const [systemStatus, setSystemStatus] = useState<string>('CONNECTING_TO_SWARM');
  const [globalScore, setGlobalScore] = useState<number>(0);
  const [modules, setModules] = useState<Record<string, ModuleState>>({});
  const [logs, setLogs] = useState<string[]>([]);

  const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_API_URL || 'http://127.0.0.1:8000';

  useEffect(() => {
    const fetchFactoryState = async () => {
      try {
        const response = await fetch(`${BACKEND_URL}/api/v1/factory/state`);
        const data = await response.json();
        setSystemStatus(data.system_status);
        setGlobalScore(data.global_score);
        setModules(data.modules);
        setLogs(data.logs);
      } catch (err) {
        console.error("Swarm connection holding or offline...", err);
      }
    };

    fetchFactoryState();
    const interval = setInterval(fetchFactoryState, 2000);
    return () => clearInterval(interval);
  }, [BACKEND_URL]);

  const handleHITLApproval = async (moduleId: string) => {
    try {
      const res = await fetch(`${BACKEND_URL}/api/v1/factory/approve/${moduleId}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
      });
      if (res.ok) alert(`HITL Verification Dispatched for ${moduleId}!`);
    } catch (err) {
      alert(`Approval synchronization loop failed connection parameters.`);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-8 font-sans">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center border-b border-slate-800 pb-6 mb-8 gap-4">
        <div>
          <h1 className="text-3xl font-black tracking-tight text-white">🤖 AGENCY FACTORY WORKSPACE</h1>
          <p className="text-slate-400 text-sm mt-1">Multi-Agent Continuous Generation System Grid</p>
        </div>
        <div className="flex gap-4">
          <div className="bg-slate-900 border border-slate-800 px-4 py-2 rounded-lg">
            <span className="block text-xs font-semibold text-slate-500 uppercase">System Status</span>
            <span className="text-sm font-bold text-amber-400">{systemStatus}</span>
          </div>
          <div className="bg-slate-900 border border-slate-800 px-4 py-2 rounded-lg text-center min-w-[100px]">
            <span className="block text-xs font-semibold text-slate-500 uppercase">Lockdown Score</span>
            <span className="text-xl font-black text-white">{globalScore}%</span>
          </div>
        </div>
      </div>

      <h2 className="text-xl font-bold mb-4 text-slate-300">Modules Implementation Architecture</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6 mb-8">
        {Object.entries(modules).map(([key, value]) => (
          <div key={key} className="bg-slate-900 border border-slate-800 rounded-xl p-5 flex flex-col justify-between hover:border-slate-700 transition-all">
            <div>
              <div className="flex justify-between items-start mb-3">
                <h3 className="font-bold text-white text-base leading-tight pr-2">{value.friendly_name}</h3>
                <span className="text-xs px-2 py-0.5 rounded-full font-semibold border bg-slate-800 text-slate-400">
                  {value.status}
                </span>
              </div>
              <div className="w-full bg-slate-800 h-2 rounded-full mb-4 overflow-hidden">
                <div className="h-full bg-blue-500 transition-all duration-500" style={{ width: `${value.progress}%` }} />
              </div>
              <div className="mb-4">
                <span className="text-xs text-slate-500 font-bold block mb-1">BOUND FILES SCOPE:</span>
                <div className="flex flex-wrap gap-1">
                  {value.files.map(f => (
                    <code key={f} className="text-xs bg-slate-950 text-blue-400 px-1.5 py-0.5 rounded border border-slate-800/60">{f}</code>
                  ))}
                </div>
              </div>
            </div>
            <button 
              onClick={() => handleHITLApproval(key)}
              className="w-full py-2 rounded-lg bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs transition-all shadow-md shadow-blue-900/20"
            >
              Execute Verification Pass
            </button>
          </div>
        ))}
      </div>

      <h2 className="text-xl font-bold mb-4 text-slate-300">Live Infrastructure Swarm Operations Trace</h2>
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 font-mono text-xs text-emerald-400 h-[250px] overflow-y-auto space-y-1.5 shadow-inner">
        {logs.map((log, index) => (
          <div key={index} className="border-b border-slate-800/30 pb-1 last:border-0">
            <span className="text-slate-500 select-none">❯</span> {log}
          </div>
        ))}
      </div>
    </div>
  );
}
