import React from 'react';

export default function Library() {
  return (
    <main>
      <section className="page-section" style={{ padding: '80px 20px', backgroundColor: '#fff' }}>
        <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
          <h1 style={{ fontSize: '48px', fontWeight: '700', color: '#062a6f', marginBottom: '40px', textAlign: 'center' }}>
            Library Services
          </h1>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '30px', marginBottom: '40px' }}>
            <div style={{ background: '#f8f9fa', padding: '30px', borderRadius: '8px', borderTop: '4px solid #062a6f' }}>
              <h2 style={{ fontSize: '24px', fontWeight: '700', color: '#062a6f', marginBottom: '12px' }}>
                Print Collections
              </h2>
              <p style={{ fontSize: '16px', color: '#555', lineHeight: '1.7' }}>
                Access to thousands of books, journals, and periodicals across multiple disciplines. 
                Our physical library houses collections spanning engineering, humanities, sciences, and more.
              </p>
            </div>

            <div style={{ background: '#f8f9fa', padding: '30px', borderRadius: '8px', borderTop: '4px solid #062a6f' }}>
              <h2 style={{ fontSize: '24px', fontWeight: '700', color: '#062a6f', marginBottom: '12px' }}>
                Digital Resources
              </h2>
              <p style={{ fontSize: '16px', color: '#555', lineHeight: '1.7' }}>
                Online access to e-books, academic databases, journals, and research papers. 
                Available 24/7 for all registered students and faculty members.
              </p>
            </div>

            <div style={{ background: '#f8f9fa', padding: '30px', borderRadius: '8px', borderTop: '4px solid #062a6f' }}>
              <h2 style={{ fontSize: '24px', fontWeight: '700', color: '#062a6f', marginBottom: '12px' }}>
                Research Support
              </h2>
              <p style={{ fontSize: '16px', color: '#555', lineHeight: '1.7' }}>
                Expert librarians and information specialists available to assist with research, 
                citation, and academic writing support.
              </p>
            </div>

            <div style={{ background: '#f8f9fa', padding: '30px', borderRadius: '8px', borderTop: '4px solid #062a6f' }}>
              <h2 style={{ fontSize: '24px', fontWeight: '700', color: '#062a6f', marginBottom: '12px' }}>
                Study Spaces
              </h2>
              <p style={{ fontSize: '16px', color: '#555', lineHeight: '1.7' }}>
                Quiet study areas, group discussion rooms, and comfortable learning spaces 
                equipped with modern technology and amenities.
              </p>
            </div>

            <div style={{ background: '#f8f9fa', padding: '30px', borderRadius: '8px', borderTop: '4px solid #062a6f' }}>
              <h2 style={{ fontSize: '24px', fontWeight: '700', color: '#062a6f', marginBottom: '12px' }}>
                Interlibrary Loan
              </h2>
              <p style={{ fontSize: '16px', color: '#555', lineHeight: '1.7' }}>
                Access materials from partner institutions. Request items not available 
                in our collection and have them delivered to you.
              </p>
            </div>

            <div style={{ background: '#f8f9fa', padding: '30px', borderRadius: '8px', borderTop: '4px solid #062a6f' }}>
              <h2 style={{ fontSize: '24px', fontWeight: '700', color: '#062a6f', marginBottom: '12px' }}>
                IT Services
              </h2>
              <p style={{ fontSize: '16px', color: '#555', lineHeight: '1.7' }}>
                Computer labs, high-speed internet, and technical support. 
                Latest software and hardware for academic and research work.
              </p>
            </div>
          </div>

          <div style={{ 
            background: '#e8f0fe', 
            padding: '30px', 
            borderRadius: '8px', 
            borderLeft: '4px solid #062a6f',
            textAlign: 'center'
          }}>
            <h2 style={{ fontSize: '24px', fontWeight: '700', color: '#062a6f', marginBottom: '16px' }}>
              Library Hours
            </h2>
            <p style={{ fontSize: '17px', color: '#333', margin: '0' }}>
              Monday - Friday: 8:00 AM - 8:00 PM<br/>
              Saturday: 9:00 AM - 5:00 PM<br/>
              Sunday: Closed
            </p>
          </div>
        </div>
      </section>
    </main>
  );
}
