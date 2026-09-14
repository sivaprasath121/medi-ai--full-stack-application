export const patientDashboard = {
  upcomingAppointment: {
    title: 'Upcoming appointment',
    value: 'Tue, 10:30 AM',
    detail: 'Cardiology follow-up',
    accent: 'emerald',
  },
  medications: {
    title: 'Current medications',
    value: '2 active',
    detail: 'Vitamin D · Levothyroxine',
    accent: 'blue',
  },
  prescriptions: {
    title: 'Recent prescriptions',
    value: '3 issued',
    detail: 'Last updated 09/08',
    accent: 'violet',
  },
  healthSummary: {
    title: 'Health summary',
    value: 'Low risk',
    detail: 'Vitals stable this month',
    accent: 'amber',
  },
  labResults: {
    title: 'Recent lab results',
    value: 'CBC normal',
    detail: 'Reviewed 2 days ago',
    accent: 'sky',
  },
  messages: {
    title: 'Messages',
    value: '3 unread',
    detail: 'Care team follow-up',
    accent: 'rose',
  },
};

export const patientTimeline = [
  { date: '2026-09-10', event: 'Consultation', kind: 'clinical-note' },
  { date: '2026-09-08', event: 'Blood Test', kind: 'lab-result' },
  { date: '2026-08-25', event: 'Prescription', kind: 'prescription' },
  { date: '2026-07-12', event: 'Appointment', kind: 'appointment' },
];

export const patientProfile = {
  full_name: 'Ava Martinez',
  date_of_birth: '1995-04-18',
  gender: 'Female',
  phone: '555-0134',
  email: 'ava.martinez@example.com',
  address: '1480 Harbor Lane, Seattle, WA',
  emergency_contact: {
    name: 'Luis Martinez',
    relationship: 'Spouse',
    phone: '555-0140',
  },
  allergies: ['Penicillin', 'Peanuts'],
  current_medications: ['Vitamin D', 'Levothyroxine'],
  previous_conditions: ['Seasonal allergies'],
  surgical_history: ['Appendectomy (2018)'],
  family_history: ['Mother: hypertension', 'Father: type 2 diabetes'],
  insurance: {
    provider: 'BlueCross Demo Plan',
    member_id: 'BC-889122',
    plan_type: 'PPO',
  },
};

export const labHistory = [
  { date: 'Jan', value: 5.2 },
  { date: 'Mar', value: 5.5 },
  { date: 'Jun', value: 5.3 },
  { date: 'Sep', value: 5.6 },
];
