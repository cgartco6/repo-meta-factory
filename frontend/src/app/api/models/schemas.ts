export interface ClientIntakeForm {
  companyName: string;
  industry: string;
  targetAudience: string;
  coreValues: string[];
  selectedTiers: 'free' | 'freemium' | 'premium';
}

export interface AgentTaskStatus {
  taskId: string;
  moduleName: 'branding' | 'design' | 'marketing';
  status: 'PENDING' | 'IN_PROCESS' | 'AWAITING_HITL' | 'COMPLETED' | 'FAILED';
  outputPayload?: any;
  errorLog?: string;
}
