import React, { useState, useEffect } from 'react';

export default function Faculties() {
  const [faculties, setFaculties] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchFaculties = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/faculties/');
        if (!response.ok) throw new Error('Failed to fetch faculties');
        const data = await response.json();
        setFaculties(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchFaculties();
  }, []);

  return (
    <main>
      <section className="page-section" style={{ padding: '80px 20px', backgroundColor: '#f8f9fa' }}>
        <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
          <h1 style={{ fontSize: '48px', fontWeight: '700', color: '#062a6f', marginBottom: '40px', textAlign: 'center' }}>
            Faculties
          </h1>

          {loading && <p style={{ textAlign: 'center', fontSize: '18px' }}>Loading faculties...</p>}
          {error && <p style={{ textAlign: 'center', color: 'red', fontSize: '18px' }}>Error: {error}</p>}

          {!loading && !error && faculties.length > 0 && (
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '30px' }}>
              {faculties.map((faculty) => (
                <div
                  key={faculty.id}
                  style={{
                    background: '#fff',
                    padding: '30px',
                    borderRadius: '8px',
                    boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
                    borderTop: '4px solid #062a6f',
                  }}
                >
                  <h2 style={{ fontSize: '24px', fontWeight: '700', color: '#062a6f', marginBottom: '12px' }}>
                    {faculty.name}
                  </h2>
                  <p style={{ fontSize: '16px', color: '#555', lineHeight: '1.7' }}>
                    {faculty.description}
                  </p>
                </div>
              ))}
            </div>
          )}

          {!loading && !error && faculties.length === 0 && (
            <p style={{ textAlign: 'center', fontSize: '18px', color: '#666' }}>No faculties available.</p>
          )}
        </div>
      </section>
    </main>
  );
}
