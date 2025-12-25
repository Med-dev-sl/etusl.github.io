import React, { useState, useEffect, useRef } from 'react';
import BiographyModal from './BiographyModal';

const PrincipalOfficers = () => {
  const [leaders, setLeaders] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const sectionRef = useRef(null);
  const [visibleCards, setVisibleCards] = useState(new Set());
  const [selectedLeader, setSelectedLeader] = useState(null);

  const openBio = (leader) => {
    setSelectedLeader(leader);
  };

  const closeBio = () => setSelectedLeader(null);

  useEffect(() => {
    const fetchLeaders = async () => {
      try {
        const response = await fetch('/api/leaders/?ordering=position__hierarchy_level,order');
        if (!response.ok) throw new Error('Failed to fetch leaders');
        const data = await response.json();
        setLeaders(data.results || data);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching leaders:', err);
        setError('Failed to load leadership data');
        setLoading(false);
      }
    };

    fetchLeaders();
  }, []);

  useEffect(() => {
    const observerOptions = {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px',
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const index = parseInt(entry.target.dataset.index, 10);
          setVisibleCards((prev) => new Set(prev).add(index));
        }
      });
    }, observerOptions);

    const cards = sectionRef.current?.querySelectorAll('[data-index]');
    cards?.forEach((card) => observer.observe(card));

    return () => {
      cards?.forEach((card) => observer.unobserve(card));
    };
  }, [leaders]);

  const groupedByHierarchy = leaders.reduce((acc, leader) => {
    const level = leader.position_level;
    if (!acc[level]) acc[level] = [];
    acc[level].push(leader);
    return acc;
  }, {});

  if (loading) {
    return <div className="principal-officers-section"><p>Loading leadership data...</p></div>;
  }

  if (error) {
    return <div className="principal-officers-section"><p>{error}</p></div>;
  }

  return (
    <section className="principal-officers-section" ref={sectionRef}>
      <div className="officers-container">
        <h2 className="section-title">Principal Officers</h2>
        
        <div className="officers-grid">
          {/* Level 1: Single Chancellor or equivalent */}
          <div className="officers-level-1">
            {groupedByHierarchy[1]?.map((leader, idx) => (
              <div
                key={leader.id}
                className={`officer-card level-1 ${
                  visibleCards.has(idx) ? 'in-view' : ''
                }`}
                data-index={idx}
                style={{
                  '--delay': `${idx * 0.1}s`,
                }}
              >
                <div className="officer-image-container">
                  {leader.photo ? (
                    <img
                      src={leader.photo}
                      alt={leader.name}
                      className="officer-photo"
                    />
                  ) : (
                    <div className="officer-photo placeholder">
                      <span>{leader.name.charAt(0)}</span>
                    </div>
                  )}
                </div>
                <h3 className="officer-name" onClick={() => openBio(leader)} role="button" tabIndex="0">{leader.name}</h3>
                <p className="officer-title" onClick={() => openBio(leader)} role="button" tabIndex="0">{leader.position_title}</p>
              </div>
            ))}
          </div>

          {/* Level 2: Middle positions */}
          <div className="officers-level-2">
            {groupedByHierarchy[2]?.map((leader, idx) => (
              <div
                key={leader.id}
                className={`officer-card level-2 ${
                  visibleCards.has(groupedByHierarchy[1]?.length + idx) ? 'in-view' : ''
                }`}
                data-index={groupedByHierarchy[1]?.length + idx}
                style={{
                  '--delay': `${(groupedByHierarchy[1]?.length + idx) * 0.1}s`,
                }}
              >
                <div className="officer-image-container">
                  {leader.photo ? (
                    <img
                      src={leader.photo}
                      alt={leader.name}
                      className="officer-photo"
                    />
                  ) : (
                    <div className="officer-photo placeholder">
                      <span>{leader.name.charAt(0)}</span>
                    </div>
                  )}
                </div>
                <h3 className="officer-name" onClick={() => openBio(leader)} role="button" tabIndex="0">{leader.name}</h3>
                <p className="officer-title" onClick={() => openBio(leader)} role="button" tabIndex="0">{leader.position_title}</p>
              </div>
            ))}
          </div>

          {/* Level 3: Directors and lower positions */}
          <div className="officers-level-3">
            {groupedByHierarchy[3]?.map((leader, idx) => (
              <div
                key={leader.id}
                className={`officer-card level-3 ${
                  visibleCards.has(
                    (groupedByHierarchy[1]?.length || 0) +
                      (groupedByHierarchy[2]?.length || 0) +
                      idx
                  )
                    ? 'in-view'
                    : ''
                }`}
                data-index={
                  (groupedByHierarchy[1]?.length || 0) +
                  (groupedByHierarchy[2]?.length || 0) +
                  idx
                }
                style={{
                  '--delay': `${
                    ((groupedByHierarchy[1]?.length || 0) +
                      (groupedByHierarchy[2]?.length || 0) +
                      idx) *
                    0.1
                  }s`,
                }}
              >
                <div className="officer-image-container">
                  {leader.photo ? (
                    <img
                      src={leader.photo}
                      alt={leader.name}
                      className="officer-photo"
                    />
                  ) : (
                    <div className="officer-photo placeholder">
                      <span>{leader.name.charAt(0)}</span>
                    </div>
                  )}
                </div>
                <h3 className="officer-name" onClick={() => openBio(leader)} role="button" tabIndex="0">{leader.name}</h3>
                <p className="officer-title" onClick={() => openBio(leader)} role="button" tabIndex="0">{leader.position_title}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
      <BiographyModal leader={selectedLeader} onClose={closeBio} />
    </section>
  );
};

export default PrincipalOfficers;
