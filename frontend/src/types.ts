export type Role = 'patient' | 'doctor' | 'admin';

export type PatientSummary = {
  id: string;
  patient_id: string;
  first_name: string;
  last_name: string;
  email: string;
  gender: string;
  date_of_birth: string;
  summary: {
    upcoming_appointment: string;
    current_medications_count: number;
    last_lab_result: string;
    risk_level: string;
  };
};

export type PatientProfile = {
  id: string;
  patient_id: string;
  first_name: string;
  last_name: string;
  email: string;
  phone: string;
  date_of_birth: string;
  gender: string;
  address: string;
  emergency_contact: {
    name: string;
    relationship: string;
    phone: string;
  };
  allergies: string[];
  current_medications: string[];
  previous_conditions: string[];
  surgical_history: string[];
  family_history: string[];
  insurance: {
    provider: string;
    member_id: string;
    plan_type: string;
  };
  summary: {
    upcoming_appointment: string;
    current_medications_count: number;
    last_lab_result: string;
    risk_level: string;
  };
};
