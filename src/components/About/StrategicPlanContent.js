import React, { useState, useEffect } from 'react';
import '../About.css';

export default function StrategicPlanContent() {
  const [plan, setPlan] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchStrategicPlan = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/strategic-plans/');
        if (!response.ok) throw new Error('Failed to fetch strategic plan');
        const data = await response.json();
        if (data && data.length > 0) {
          setPlan(data[0]);
        }
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchStrategicPlan();
  }, []);

  if (loading) {
    return <div className="strategic-content-loading">Loading strategic plan...</div>;
  }

  if (error || !plan) {
    return <div className="strategic-content-error">Unable to load strategic plan content</div>;
  }

  return (
    <div className="strategic-plan-container">
      {plan.sections && plan.sections.map((section, idx) => {
        if (section.section_type === 'overview') {
          return <OverviewSection key={idx} section={section} />;
        } else if (section.section_type === 'vision_commitment') {
          return <VisionCommitmentsSection key={idx} section={section} />;
        } else if (section.section_type === 'objectives') {
          return <ObjectivesSection key={idx} section={section} />;
        } else if (section.section_type === 'goals') {
          return <GoalsSection key={idx} section={section} />;
        }
        return null;
      })}
    </div>
  );
}

function OverviewSection({ section }) {
  return (
    <section className="strategic-overview">
      <div className="strategic-container">
        <div className="overview-grid">
          {section.image && (
            <div className="overview-image-wrapper">
              <img src={section.image} alt={section.heading} className="overview-image" />
            </div>
          )}
          <div className="overview-content-wrapper">
            <h2 className="strategic-heading">{section.heading}</h2>
            <div className="overview-text">
              {section.content.split('\n\n').map((para, idx) => (
                <p key={idx}>{para}</p>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

function VisionCommitmentsSection({ section }) {
  return (
    <section className="strategic-vision-section">
      <div className="strategic-container">
        <h2 className="strategic-section-title">{section.heading}</h2>
        <p className="strategic-section-subtitle">{section.subheading}</p>

        <div className="vision-commitments-list">
          {section.items && section.items.map((item, idx) => (
            <div key={idx} className="commitment-item">
              <div className="commitment-bullet">•</div>
              <div className="commitment-text">
                <strong>{item.title}</strong> {item.description}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function ObjectivesSection({ section }) {
  return (
    <section className="strategic-objectives-section">
      <div className="strategic-container">
        <h2 className="strategic-section-title">{section.heading}</h2>
        <div className="objectives-content">
          <p>{section.content}</p>
        </div>
      </div>
    </section>
  );
}

function GoalsSection({ section }) {
  const isMultipleGoals = section.items && section.items.length > 3;
  const gridClass = isMultipleGoals ? 'goals-grid-4' : 'goals-grid-3';

  return (
    <section className="strategic-goals-section">
      <div className="strategic-container">
        <h2 className="strategic-section-title">{section.heading}</h2>
        {section.subheading && <p className="goals-subtitle">{section.subheading}</p>}
        {section.content && <div className="goals-description">{section.content}</div>}

        {section.items && section.items.length > 0 && (
          <div className={`goals-grid ${gridClass}`}>
            {section.items.map((item, idx) => (
              <div key={idx} className="goal-card">
                <div className="goal-number">{item.goal}</div>
                <h3 className="goal-title">{item.title}</h3>
                <p className="goal-description">{item.description}</p>
              </div>
            ))}
          </div>
        )}
      </div>
    </section>
  );
}
