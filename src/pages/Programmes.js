import React from 'react';

export default function Programmes() {
  return (
    <main>
      <section className="page-section" style={{ padding: '80px 20px', backgroundColor: '#fff' }}>
        <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
          <h1 style={{ fontSize: '48px', fontWeight: '700', color: '#062a6f', marginBottom: '40px', textAlign: 'center' }}>
            Academic Programmes
          </h1>

          <div style={{ 
            background: '#f8f9fa', 
            padding: '40px', 
            borderRadius: '8px', 
            borderLeft: '4px solid #062a6f',
            marginBottom: '40px'
          }}>
            <h2 style={{ fontSize: '28px', fontWeight: '700', color: '#062a6f', marginBottom: '16px' }}>
              Undergraduate Programmes
            </h2>
            <p style={{ fontSize: '17px', color: '#555', lineHeight: '1.8' }}>
              We offer a variety of undergraduate programmes designed to equip students with theoretical knowledge 
              and practical skills for their chosen careers. Our programmes span across engineering, humanities, sciences, 
              business, and more.
            </p>
          </div>

          <div style={{ 
            background: '#f8f9fa', 
            padding: '40px', 
            borderRadius: '8px', 
            borderLeft: '4px solid #062a6f',
            marginBottom: '40px'
          }}>
            <h2 style={{ fontSize: '28px', fontWeight: '700', color: '#062a6f', marginBottom: '16px' }}>
              Postgraduate Programmes
            </h2>
            <p style={{ fontSize: '17px', color: '#555', lineHeight: '1.8' }}>
              Our postgraduate programmes are designed for professionals seeking to advance their careers with specialized 
              knowledge and research opportunities. We offer master's and doctoral degrees across multiple disciplines.
            </p>
          </div>

          <div style={{ 
            background: '#f8f9fa', 
            padding: '40px', 
            borderRadius: '8px', 
            borderLeft: '4px solid #062a6f'
          }}>
            <h2 style={{ fontSize: '28px', fontWeight: '700', color: '#062a6f', marginBottom: '16px' }}>
              Certificate & Diploma Programmes
            </h2>
            <p style={{ fontSize: '17px', color: '#555', lineHeight: '1.8' }}>
              Short-term certificate and diploma programmes provide focused training in specific skill areas. 
              These programmes are ideal for professionals looking to upskill or gain certification in their field.
            </p>
          </div>
        </div>
      </section>
    </main>
  );
}
