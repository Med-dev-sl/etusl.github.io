import React, { useEffect, useState } from 'react';
import '../About.css';

export default function History() {
	const [historyData, setHistoryData] = useState(null);
	const [loading, setLoading] = useState(true);
	const [error, setError] = useState(null);
	const [visibleSections, setVisibleSections] = useState({});

	useEffect(() => {
		const fetchHistory = async () => {
			try {
				// Fetch history data from backend
				const response = await fetch('http://127.0.0.1:8000/api/about-history/');
				if (!response.ok) throw new Error('Failed to fetch history');
				const data = await response.json();
				// Handle paginated or direct response
				const histories = Array.isArray(data) ? data : (data.results || [data]);
				setHistoryData(histories[0] || null);
			} catch (err) {
				setError(err.message);
				console.error('Error fetching history:', err);
			} finally {
				setLoading(false);
			}
		};

		fetchHistory();
	}, []);

	// Intersection Observer for animations
	useEffect(() => {
		const observer = new IntersectionObserver((entries) => {
			entries.forEach((entry) => {
				if (entry.isIntersecting) {
					setVisibleSections(prev => ({
						...prev,
						[entry.target.id]: true
					}));
					observer.unobserve(entry.target);
				}
			});
		}, { threshold: 0.1 });

		// Observe all sections with animation
		document.querySelectorAll('[data-animate-history]').forEach(el => {
			observer.observe(el);
		});

		return () => observer.disconnect();
	}, [historyData]);

	if (loading) return <div className="history-loading">Loading...</div>;
	if (error) return <div className="history-error">Error: {error}</div>;
	if (!historyData) {
		return (
			<section className="history-section" aria-label="History">
				<div className="history-container">
					<div className="history-content">
						<header className="history-header">
							<h2 className="history-title">History</h2>
						</header>
						<div className="history-description">
							<p>
								The history content will be displayed here once added to the administration panel.
							</p>
						</div>
					</div>
				</div>
			</section>
		);
	}

	return (
		<>
			{/* Main History Section with Image and Text */}
			{historyData.content && (
				<section 
					id="history-main"
					className="history-section" 
					aria-label="History Content"
					data-animate-history
					style={{
						opacity: visibleSections['history-main'] ? 1 : 0,
						transform: visibleSections['history-main'] ? 'translateY(0)' : 'translateY(40px)',
						transition: 'all 0.9s cubic-bezier(0.34, 1.56, 0.64, 1)',
					}}
				>
					<div className="history-container">
						<div className="history-main-grid">
							{/* Left Column: Title and Image */}
							<div className="history-left-column">
								<h2 className="history-main-title">{historyData.title || 'History'}</h2>
								{historyData.image && (
									<div className="history-featured-image-wrapper">
										<img 
											src={historyData.image} 
											alt={historyData.title || 'History'} 
											className="history-featured-image"
										/>
									</div>
								)}
							</div>

							{/* Right Column: Main Text */}
							<div className="history-right-column">
								{historyData.subtitle && (
									<p className="history-intro-text">{historyData.subtitle}</p>
								)}
								<div 
									className="history-main-text" 
									dangerouslySetInnerHTML={{ __html: historyData.content }}
								/>
							</div>
						</div>
					</div>
				</section>
			)}

			{/* History Events Timeline */}
			{historyData.events && historyData.events.length > 0 && (
				<section 
					id="history-timeline"
					className="history-timeline-section" 
					aria-label="History Timeline"
					data-animate-history
					style={{
						opacity: visibleSections['history-timeline'] ? 1 : 0,
						transform: visibleSections['history-timeline'] ? 'translateY(0)' : 'translateY(40px)',
						transition: 'all 0.9s cubic-bezier(0.34, 1.56, 0.64, 1)',
					}}
				>
					<div className="history-container">
						<h2 className="timeline-title">Key Milestones</h2>
						<div className="timeline">
							{historyData.events.map((event, idx) => (
								<div 
									key={event.id} 
									className="timeline-item"
									style={{
										opacity: visibleSections['history-timeline'] ? 1 : 0,
										transform: visibleSections['history-timeline'] ? 'translateY(0)' : 'translateY(20px)',
										transition: `all 0.7s cubic-bezier(0.34, 1.56, 0.64, 1) ${idx * 0.1}s`,
									}}
								>
									<div className="timeline-marker">
										<div className="marker-dot"></div>
									</div>
									<div className="timeline-content">
										<div className="timeline-year">{event.year || `Event ${idx + 1}`}</div>
										<h3 className="timeline-event-title">{event.title || event.name}</h3>
										{event.description && (
											<p className="timeline-description">{event.description}</p>
										)}
									</div>
								</div>
							))}
						</div>
					</div>
				</section>
			)}

			{/* History Images Gallery */}
			{historyData.images && historyData.images.length > 0 && (
				<section 
					id="history-gallery"
					className="history-gallery-section" 
					aria-label="History Gallery"
					data-animate-history
					style={{
						opacity: visibleSections['history-gallery'] ? 1 : 0,
						transform: visibleSections['history-gallery'] ? 'translateY(0)' : 'translateY(40px)',
						transition: 'all 0.9s cubic-bezier(0.34, 1.56, 0.64, 1)',
					}}
				>
					<div className="history-container">
						<h2 className="gallery-title">Through the Years</h2>
						<div className="history-images-grid">
							{historyData.images.map((img, idx) => (
								<div 
									key={img.id} 
									className="history-gallery-item"
									style={{
										opacity: visibleSections['history-gallery'] ? 1 : 0,
										transform: visibleSections['history-gallery'] ? 'scale(1)' : 'scale(0.9)',
										transition: `all 0.7s cubic-bezier(0.34, 1.56, 0.64, 1) ${idx * 0.08}s`,
									}}
								>
									{img.image ? (
										<img src={img.image} alt={img.caption || 'History'} className="history-gallery-image" />
									) : (
										<div className="history-image-placeholder">
											<span>No image</span>
										</div>
									)}
									{img.caption && <p className="history-image-caption">{img.caption}</p>}
									{img.year && <span className="history-image-year">{img.year}</span>}
								</div>
							))}
						</div>
					</div>
				</section>
			)}
		</>
	);
}

