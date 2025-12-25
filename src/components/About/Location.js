import React, { useState } from 'react';
import '../About.css';

export default function Location() {
  const [isETU, setIsETU] = useState(false);

  const UG_IMAGE = 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=1400&h=420&fit=crop';
  const ETU_IMAGE = 'https://images.unsplash.com/photo-1473172707857-f9e276582ab6?w=1400&h=420&fit=crop';

  const UG_MAP = 'https://www.google.com/maps/place/Eastern+Technical+University/@7.8762763,-11.1823188,17z/data=!3m1!4b1!4m6!3m5!1s0xf07cf3875bea735:0xb537772487d716d5!8m2!3d7.8762763!4d-11.1823188!16s%2Fg%2F11rf9x5b5l?entry=ttu&g_ep=EgoyMDI1MTIwOS4wIKXMDSoASAFQAw%3D%3D';
  const ETU_MAP = 'https://www.google.com/maps/place/Eastern+Technical+University/@7.8762763,-11.1823188,17z/data=!3m1!4b1!4m6!3m5!1s0xf07cf3875bea735:0xb537772487d716d5!8m2!3d7.8762763!4d-11.1823188!16s%2Fg%2F11rf9x5b5l?entry=ttu&g_ep=EgoyMDI1MTIwOS4wIKXMDSoASAFQAw%3D%3D';

  const openMap = () => {
    const url = isETU ? ETU_MAP : UG_MAP;
    window.open(url, '_blank', 'noopener,noreferrer');
  };

  return (
    <section
      className="location-hero"
      style={{ backgroundImage: `url(${isETU ? ETU_IMAGE : UG_IMAGE})` }}
      aria-label="Our Location"
    >
      <div className="location-overlay" />

      <div className="location-content">
        <h2 className="location-title">OUR LOCATION</h2>
        <p className="location-subtitle">
          {isETU
            ? 'Eastern Technical University of Sierra Leone is located in Freetown, Sierra Leone.'
            : 'The Eastern Technical University, is located in Sierra Leone, Kenema.'}
        </p>

        <div style={{ display: 'flex', gap: 12, justifyContent: 'center', alignItems: 'center', flexWrap: 'wrap' }}>
          <button
            className="location-button"
            onClick={openMap}
            aria-pressed={isETU}
            type="button"
          >
            <span className="location-button-text">
              {isETU ? 'Map of ETU Main Campus' : 'Map of ETU Main Campus'}
            </span>
            <span className="location-button-arrow">›</span>
          </button>

          <button
            className="location-toggle-link"
            onClick={() => setIsETU((v) => !v)}
            type="button"
            aria-label="Toggle campus view"
          >
            {isETU ? 'Show ETU view' : 'Show ETU view'}
          </button>
        </div>
      </div>
    </section>
  );
}
