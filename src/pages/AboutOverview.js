import React, { useEffect, useState } from 'react';
import '../components/About/About.css';
import OverView from '../components/About/overView';

export default function AboutOverview() {
  const [heroImage, setHeroImage] = useState(
    'https://images.unsplash.com/photo-1427504494785-cdee0fbb0d5e?w=1200&h=600&fit=crop'
  );

  return (
    <main>
      {/* Hero Section */}
      <section 
        className="overview-hero"
        style={{
          backgroundImage: `url(${heroImage})`,
          backgroundSize: 'cover',
          backgroundPosition: 'center',
          backgroundAttachment: 'fixed',
          minHeight: '600px',
          position: 'relative',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'flex-start',
          paddingLeft: '60px',
        }}
        aria-label="University Overview Hero"
      >
        {/* Overlay for text readability */}
        <div
          style={{
            position: 'absolute',
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            background: 'linear-gradient(135deg, rgba(0, 0, 0, 0.35) 0%, rgba(0, 0, 0, 0.25) 100%)',
            zIndex: 1,
          }}
        />
        
        {/* Hero Content */}
        <div style={{ position: 'relative', zIndex: 2, color: '#ffffff', maxWidth: '600px' }}>
          <h1 
            style={{
              fontSize: '72px',
              fontWeight: '700',
              marginBottom: '20px',
              lineHeight: '1.1',
              animation: 'slideInFromLeft 1s ease-out',
            }}
          >
            Discover
          </h1>
          <h2 
            style={{
              fontSize: '56px',
              fontWeight: '600',
              marginBottom: '30px',
              lineHeight: '1.2',
              color: '#f0f0f0',
              animation: 'slideInFromLeft 1.2s ease-out',
            }}
          >
           Eastern Technical University
          </h2>
          <p 
            style={{
              fontSize: '18px',
              fontWeight: '300',
              lineHeight: '1.6',
              maxWidth: '500px',
              animation: 'slideInFromLeft 1.4s ease-out',
            }}
          >
            Excellence in academic and professional education with world-class facilities and experienced faculty.
          </p>
        </div>
      </section>

      {/* Overview Content Section */}
      <OverView />
    </main>
  );
}
