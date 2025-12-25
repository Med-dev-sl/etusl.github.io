import React, { useEffect, useState } from 'react';
import '../About.css';

export default function OverView() {
	const [overviewData, setOverviewData] = useState(null);
	const [loading, setLoading] = useState(true);
	const [error, setError] = useState(null);
	const [visibleSections, setVisibleSections] = useState({});

	useEffect(() => {
		const fetchOverview = async () => {
			try {
				// Fetch the first/main about overview (assumes admin creates one)
				const response = await fetch('http://127.0.0.1:8000/api/about-overviews/');
				if (!response.ok) throw new Error('Failed to fetch overview');
				const data = await response.json();
				// If paginated, get results; otherwise use data directly
				const overviews = data.results || data;
				setOverviewData(overviews[0] || null);
			} catch (err) {
				setError(err.message);
				console.error('Error fetching overview:', err);
			} finally {
				setLoading(false);
			}
		};

		fetchOverview();
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
		document.querySelectorAll('[data-animate]').forEach(el => {
			observer.observe(el);
		});

		return () => observer.disconnect();
	}, [overviewData]);

	if (loading) return <div className="overview-loading">Loading...</div>;
	if (error) return <div className="overview-error">Error: {error}</div>;
	if (!overviewData) return <div className="overview-empty">No overview data available</div>;

	return (
		<>
			{/* Profile Section: Brief + Statistics */}
			<section 
				id="profile-section"
				className="overview-profile" 
				aria-label="University Profile"
				data-animate
				style={{
					opacity: visibleSections['profile-section'] ? 1 : 0,
					transform: visibleSections['profile-section'] ? 'translateY(0)' : 'translateY(30px)',
					transition: 'all 0.8s cubic-bezier(0.34, 1.56, 0.64, 1)'
				}}
			>
				<div className="overview-container">
					<div className="profile-brief">
						<h2 className="profile-title">Profile</h2>
						<div className="profile-text" dangerouslySetInnerHTML={{ __html: overviewData.brief }} />
					</div>
					<div className="profile-statistics">
						{overviewData.stat_items && overviewData.stat_items.length > 0 ? (
							<>
								{overviewData.stat_items.map((stat, idx) => (
									<div 
										key={stat.id} 
										className="stat-card"
										style={{
											opacity: visibleSections['profile-section'] ? 1 : 0,
											transform: visibleSections['profile-section'] ? 'translateY(0)' : 'translateY(20px)',
											transition: `all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1) ${idx * 0.1}s`,
											transitionDelay: visibleSections['profile-section'] ? `${idx * 0.1}s` : '0s'
										}}
									>
										<div className="stat-value">{stat.value}</div>
										<div className="stat-label">{stat.label}</div>
									</div>
								))}
								<div className="stats-view-all">
									<a href="/about-statistics" title="View all university statistics">See all UG Statistics</a>
								</div>
							</>
						) : (
							<p>No statistics available</p>
						)}
					</div>
				</div>
			</section>

			{/* Campuses Section */}
			{overviewData.campuses && overviewData.campuses.length > 0 && (
				<section 
					id="campuses-section"
					className="overview-campuses" 
					aria-label="Our Campuses"
					data-animate
					style={{
						opacity: visibleSections['campuses-section'] ? 1 : 0,
						transform: visibleSections['campuses-section'] ? 'translateY(0)' : 'translateY(30px)',
						transition: 'all 0.8s cubic-bezier(0.34, 1.56, 0.64, 1)'
					}}
				>
					<div className="overview-container">
						<h2 className="section-title">Our Campuses</h2>
						<div className="campuses-grid">
							{overviewData.campuses.map((campus, idx) => (
								<div 
									key={campus.id} 
									className="campus-card"
									style={{
										opacity: visibleSections['campuses-section'] ? 1 : 0,
										transform: visibleSections['campuses-section'] ? 'scale(1)' : 'scale(0.95)',
										transition: `all 0.7s cubic-bezier(0.34, 1.56, 0.64, 1) ${idx * 0.15}s`
									}}
								>
									{campus.image ? (
										<div className="campus-image-wrapper">
											<img src={campus.image} alt={campus.name} className="campus-image" />
											<div className="campus-overlay">
												<h3 className="campus-name">{campus.name}</h3>
											</div>
										</div>
									) : (
										<div className="campus-image-placeholder">
											<span>No image available</span>
										</div>
									)}
									{campus.description && (
										<p className="campus-description">{campus.description}</p>
									)}
								</div>
							))}
						</div>
					</div>
				</section>
			)}

			{/* Content Section */}
			{overviewData.content && (
				<section 
					id="content-section"
					className="overview-content" 
					aria-label="Overview Content"
					data-animate
					style={{
						opacity: visibleSections['content-section'] ? 1 : 0,
						transform: visibleSections['content-section'] ? 'translateY(0)' : 'translateY(30px)',
						transition: 'all 0.8s cubic-bezier(0.34, 1.56, 0.64, 1)'
					}}
				>
					<div className="overview-container">
						<div className="content-text" dangerouslySetInnerHTML={{ __html: overviewData.content }} />
					</div>
				</section>
			)}

			{/* Images Gallery Section */}
			{overviewData.images && overviewData.images.length > 0 && (
				<section 
					id="gallery-section"
					className="overview-gallery" 
					aria-label="University Gallery"
					data-animate
					style={{
						opacity: visibleSections['gallery-section'] ? 1 : 0,
						transform: visibleSections['gallery-section'] ? 'translateY(0)' : 'translateY(30px)',
						transition: 'all 0.8s cubic-bezier(0.34, 1.56, 0.64, 1)'
					}}
				>
					<div className="overview-container">
						<h2 className="section-title">University Gallery</h2>
						<div className="images-grid">
							{overviewData.images.map((img, idx) => (
								<div 
									key={img.id} 
									className="gallery-item"
									style={{
										opacity: visibleSections['gallery-section'] ? 1 : 0,
										transform: visibleSections['gallery-section'] ? 'translateY(0)' : 'translateY(20px)',
										transition: `all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1) ${idx * 0.08}s`
									}}
								>
									{img.image ? (
										<img src={img.image} alt={img.caption || 'Gallery'} className="gallery-image" />
									) : (
										<div className="gallery-image-placeholder">
											<span>No image</span>
										</div>
									)}
									{img.caption && <p className="gallery-caption">{img.caption}</p>}
								</div>
							))}
						</div>
					</div>
				</section>
			)}
		</>
	);
}

