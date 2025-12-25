import React, { useState, useEffect } from 'react';
import './AcademicsOverview.css';

export default function AcademicsOverview() {
  const [pageContent, setPageContent] = useState(null);
  const [statistics, setStatistics] = useState([]);
  const [admissions, setAdmissions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Fetch academic page content
        const pageRes = await fetch('http://127.0.0.1:8000/api/academic-pages/1/');
        if (!pageRes.ok) {
          throw new Error('Failed to fetch academic page');
        }
        const pageData = await pageRes.json();
        setPageContent(pageData);

        // Fetch academic statistics
        const statsRes = await fetch('http://127.0.0.1:8000/api/academic-statistics/');
        const statsData = await statsRes.json();
        setStatistics(Array.isArray(statsData) ? statsData : []);

        // Fetch admission types
        const admissionsRes = await fetch('http://127.0.0.1:8000/api/admission-types/');
        const admissionsData = await admissionsRes.json();
        setAdmissions(Array.isArray(admissionsData) ? admissionsData : []);

        setLoading(false);
      } catch (err) {
        console.error('Error fetching academics data:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  // Intersection observer for animations
  useEffect(() => {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    const cards = document.querySelectorAll('[data-animate]');
    cards.forEach((card) => {
      observer.observe(card);
    });

    return () => {
      observer.disconnect();
    };
  }, [statistics, admissions]);

  if (loading) {
    return (
      <main style={{ padding: '40px 20px', textAlign: 'center' }}>
        <p>Loading academics information...</p>
      </main>
    );
  }

  if (error) {
    return (
      <main style={{ padding: '40px 20px', textAlign: 'center' }}>
        <p>Error loading data: {error}</p>
      </main>
    );
  }

  return (
    <main>
      {/* Hero Section */}
      <section className="academics-hero">
        <div 
          className="academics-hero__background" 
          style={{ 
            backgroundImage: 'url(https://images.unsplash.com/photo-1523580494863-6f3031224c94?w=1200&h=600&fit=crop)',
            backgroundPosition: 'center',
            backgroundSize: 'cover',
            backgroundRepeat: 'no-repeat'
          }}
        />
        <div className="academics-hero__overlay" />
        <div className="academics-hero__content">
          <h1 className="academics-hero__title">{pageContent?.page_title || 'Academics'}</h1>
          <p className="academics-hero__subtitle">
            {pageContent?.hero_subtitle || 'Academic work is one of the most crucial aspects of the university experience.'}
          </p>
        </div>
      </section>

      {/* Overview Section */}
      <section className="academics-overview">
        <div className="container">
          <h2 className="section-title">{pageContent?.overview_title}</h2>
          <p className="section-description">
            {pageContent?.overview_description}
          </p>
        </div>
      </section>

      {/* Statistics Section */}
      {statistics.length > 0 && (
        <section className="academics-statistics">
          <div className="container">
            <div className="statistics-grid">
              {statistics.map((stat, index) => (
                <div 
                  key={stat.id} 
                  className="statistic-card"
                  data-animate
                  style={{ animationDelay: `${index * 100}ms` }}
                >
                  <div className="statistic-value">{stat.value}</div>
                  <div className="statistic-label">{stat.label}</div>
                </div>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* Admissions Section */}
      {admissions.length > 0 && (
        <section className="academics-admissions">
          <div className="container">
            <h2 className="section-title admissions-title">Admissions</h2>
            <div className="admissions-grid">
              {admissions.map((admission, index) => (
                <div 
                  key={admission.id}
                  className="admission-card"
                  data-animate
                  style={{ animationDelay: `${index * 100}ms` }}
                >
                  <div className="admission-card__image">
                    {admission.image_url ? (
                      <img 
                        src={admission.image_url} 
                        alt={admission.title}
                        loading="lazy"
                      />
                    ) : (
                      <div className="admission-card__placeholder">
                        {admission.title}
                      </div>
                    )}
                  </div>
                  <div className="admission-card__overlay" />
                  <div className="admission-card__content">
                    <h3>{admission.title}</h3>
                    {admission.link_url && (
                      <a href={admission.link_url} className="admission-card__link">
                        Learn More →
                      </a>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* Nurturing Success Section */}
      <section className="academics-nurture">
        <div className="container">
          <div className="nurture-content">
            <h2 className="section-title" data-animate>{pageContent?.nurture_title}</h2>
            <p className="nurture-description" data-animate>
              {pageContent?.nurture_description}
            </p>
            {pageContent?.study_with_us_link && (
              <a href={pageContent.study_with_us_link} className="cta-button" data-animate>
                Study with us →
              </a>
            )}
          </div>
        </div>
      </section>

      {/* Student Resources Section */}
      <section className="academics-resources">
        <div className="container">
          <div className="resources-grid">
            {/* Academic Calendar */}
            <div className="resource-card" data-animate>
              <h3>{pageContent?.academic_calendar_title}</h3>
              <p>{pageContent?.academic_calendar_description}</p>
              {pageContent?.academic_calendar_link && (
                <a href={pageContent.academic_calendar_link} className="resource-link">
                  Browse Academic Calendar →
                </a>
              )}
            </div>

            {/* Student Handbook */}
            {pageContent?.student_handbook_link && (
              <div className="resource-card" data-animate>
                <h3>Student Handbook</h3>
                <p>Access comprehensive guidelines and policies for students</p>
                <a href={pageContent.student_handbook_link} className="resource-link">
                  View Student Handbook →
                </a>
              </div>
            )}
          </div>
        </div>
      </section>
    </main>
  );
}
