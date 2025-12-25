import React, { useEffect, useState } from 'react';
import Leadership from '../components/About/leadershipDirectorates';
import '../components/About/About.css';

export default function AboutLeadership() {
  const [heroImage, setHeroImage] = useState(
    'https://images.unsplash.com/photo-1552664730-d307ca884978?w=1200&h=600&fit=crop'
  );
  const [animateHero, setAnimateHero] = useState(false);

  useEffect(() => {
    setAnimateHero(true);
  }, []);

  return (
    <main>
      {/* Hero Section */}
      <section 
        className="leadership-hero"
        style={{
          backgroundImage: `url(${heroImage})`,
          backgroundSize: 'cover',
          backgroundPosition: 'center',
          backgroundAttachment: 'fixed',
          minHeight: '500px',
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
        aria-label="University Leadership and Administration"
      >
        {/* Dark Overlay */}
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
            maxWidth: '700px',
          }}
        >
          <h1 
            style={{
              fontSize: '56px',
              fontWeight: '700',
              marginBottom: '20px',
              lineHeight: '1.2',
              animation: animateHero ? 'slideInFromLeft 1s cubic-bezier(0.34, 1.56, 0.64, 1) 0.3s both' : 'none',
            }}
          >
            University Leadership and Administration
          </h1>
          <p 
            style={{
              fontSize: '18px',
              fontWeight: '300',
              lineHeight: '1.6',
              maxWidth: '600px',
              animation: animateHero ? 'slideInFromLeft 1.2s cubic-bezier(0.34, 1.56, 0.64, 1) 0.5s both' : 'none',
            }}
          >
            Driving ETU's Vision: Meet the leadership and administrative directorates, who are dedicated to inspiring excellence and innovation throughout the university.
          </p>
        </div>
      </section>

      {/* Leadership Content */}
      <Leadership />
    </main>
  );
}
