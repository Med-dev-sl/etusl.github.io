import React from 'react';
import Hero from '../components/Hero';
import './Home.css';

function Home() {
  return (
    <div className="home">
      <Hero />

      <section className="features">
        <div className="features__container">
          <div className="feature-card">
            <h3>Quality Education</h3>
            <p>Comprehensive academic programs designed to prepare students for success.</p>
          </div>
          <div className="feature-card">
            <h3>Expert Faculty</h3>
            <p>Learn from experienced educators and industry professionals.</p>
          </div>
          <div className="feature-card">
            <h3>Modern Facilities</h3>
            <p>Access state-of-the-art resources and learning environments.</p>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Home;
