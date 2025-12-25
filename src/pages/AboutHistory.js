import React, { useEffect, useState } from 'react';
import History from '../components/About/history';
import Location from '../components/About/Location';
import '../components/About/About.css';

export default function AboutHistory() {
  const [heroImage, setHeroImage] = useState(
    'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=1200&h=600&fit=crop'
  );
  const [animateHero, setAnimateHero] = useState(false);

  useEffect(() => {
    // Trigger animation on mount
    setAnimateHero(true);
  }, []);

  return (
    <main>
      {/* Hero Section with Slide Down Animation */}
      <section 
        className="history-hero"
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
          overflow: 'hidden',
          opacity: animateHero ? 1 : 0,
          transform: animateHero ? 'translateY(0)' : 'translateY(-80px)',
          transition: 'all 1s cubic-bezier(0.34, 1.56, 0.64, 1)',
        }}
        aria-label="University History Hero"
      >
        {/* Overlay for text readability */}
        <div
          style={{
            position: 'absolute',
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            background: 'linear-gradient(135deg, rgba(6, 42, 111, 0.5) 0%, rgba(6, 42, 111, 0.4) 100%)',
            zIndex: 1,
          }}
        />
        
        {/* Hero Content */}
        <div 
          style={{ 
            position: 'relative', 
            zIndex: 2, 
            color: '#ffffff', 
            maxWidth: '600px',
            animation: animateHero ? 'slideInFromLeft 1.2s cubic-bezier(0.34, 1.56, 0.64, 1) 0.2s both' : 'none',
          }}
        >
          <h1 
            style={{
              fontSize: '72px',
              fontWeight: '700',
              marginBottom: '20px',
              lineHeight: '1.1',
              animation: animateHero ? 'slideInFromLeft 1s cubic-bezier(0.34, 1.56, 0.64, 1) 0.3s both' : 'none',
            }}
          >
            The History
          </h1>
          <h2 
            style={{
              fontSize: '56px',
              fontWeight: '600',
              marginBottom: '30px',
              lineHeight: '1.2',
              color: '#f0f0f0',
              animation: animateHero ? 'slideInFromLeft 1.2s cubic-bezier(0.34, 1.56, 0.64, 1) 0.5s both' : 'none',
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
              animation: animateHero ? 'slideInFromLeft 1.4s cubic-bezier(0.34, 1.56, 0.64, 1) 0.7s both' : 'none',
            }}
          >
            Discover the heritage and legacy of Sierra Leone's premier institution of higher learning.
          </p>
        </div>
      </section>

      {/* History Content */}
      <History />

      {/* Location section placed just above the footer */}
      <Location />
    </main>
  );
}
