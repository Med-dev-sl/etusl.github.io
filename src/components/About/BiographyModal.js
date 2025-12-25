import React from 'react';
import '../About/About.css';

const BiographyModal = ({ leader, onClose }) => {
  if (!leader) return null;

  return (
    <div className="bio-modal-overlay" onClick={onClose} role="dialog" aria-modal="true">
      <div className="bio-modal" onClick={(e) => e.stopPropagation()}>
        <button className="bio-close" onClick={onClose} aria-label="Close biography">×</button>
        <div className="bio-grid">
          <div className="bio-photo-col">
            {leader.photo ? (
              <img src={leader.photo} alt={leader.name} className="bio-photo" />
            ) : (
              <div className="bio-photo placeholder"><span>{leader.name?.charAt(0)}</span></div>
            )}
          </div>
          <div className="bio-content-col">
            <h2 className="bio-name">{leader.name}</h2>
            <p className="bio-position">{leader.position_title}</p>
            {leader.bio ? (
              <div className="bio-text" dangerouslySetInnerHTML={{ __html: leader.bio }} />
            ) : (
              <p className="bio-text">No biography available.</p>
            )}
            <div className="bio-contact">
              {leader.email && <p><strong>Email:</strong> <a href={`mailto:${leader.email}`}>{leader.email}</a></p>}
              {leader.phone && <p><strong>Phone:</strong> {leader.phone}</p>}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default BiographyModal;
