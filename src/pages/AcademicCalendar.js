import React from 'react';

export default function AcademicCalendar() {
  return (
    <main>
      <section className="page-section" style={{ padding: '80px 20px', backgroundColor: '#f8f9fa' }}>
        <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
          <h1 style={{ fontSize: '48px', fontWeight: '700', color: '#062a6f', marginBottom: '40px', textAlign: 'center' }}>
            Academic Calendar
          </h1>

          <div style={{ background: '#fff', padding: '40px', borderRadius: '8px', boxShadow: '0 2px 8px rgba(0,0,0,0.1)' }}>
            <table style={{ width: '100%', borderCollapse: 'collapse' }}>
              <thead>
                <tr style={{ backgroundColor: '#062a6f', color: 'white' }}>
                  <th style={{ padding: '15px', textAlign: 'left', fontWeight: '700' }}>Event</th>
                  <th style={{ padding: '15px', textAlign: 'left', fontWeight: '700' }}>Date</th>
                  <th style={{ padding: '15px', textAlign: 'left', fontWeight: '700' }}>Description</th>
                </tr>
              </thead>
              <tbody>
                <tr style={{ borderBottom: '1px solid #ddd' }}>
                  <td style={{ padding: '15px', fontWeight: '600' }}>Academic Year Begins</td>
                  <td style={{ padding: '15px' }}>September 1</td>
                  <td style={{ padding: '15px', color: '#666' }}>First day of classes for all students</td>
                </tr>
                <tr style={{ borderBottom: '1px solid #ddd' }}>
                  <td style={{ padding: '15px', fontWeight: '600' }}>Midterm Examinations</td>
                  <td style={{ padding: '15px' }}>October 15 - November 15</td>
                  <td style={{ padding: '15px', color: '#666' }}>Midterm assessment period</td>
                </tr>
                <tr style={{ borderBottom: '1px solid #ddd' }}>
                  <td style={{ padding: '15px', fontWeight: '600' }}>Semester Break</td>
                  <td style={{ padding: '15px' }}>December 1 - January 15</td>
                  <td style={{ padding: '15px', color: '#666' }}>Holiday and break period</td>
                </tr>
                <tr style={{ borderBottom: '1px solid #ddd' }}>
                  <td style={{ padding: '15px', fontWeight: '600' }}>Final Examinations</td>
                  <td style={{ padding: '15px' }}>April 1 - May 15</td>
                  <td style={{ padding: '15px', color: '#666' }}>End of year assessment period</td>
                </tr>
                <tr>
                  <td style={{ padding: '15px', fontWeight: '600' }}>Graduation Ceremony</td>
                  <td style={{ padding: '15px' }}>June 15</td>
                  <td style={{ padding: '15px', color: '#666' }}>Annual graduation ceremony</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div style={{ marginTop: '40px', padding: '30px', background: '#e8f0fe', borderRadius: '8px', borderLeft: '4px solid #062a6f' }}>
            <p style={{ fontSize: '16px', color: '#333', margin: '0' }}>
              <strong>Note:</strong> The academic calendar is subject to change. Please contact the Registrar's Office for 
              the most updated information.
            </p>
          </div>
        </div>
      </section>
    </main>
  );
}
