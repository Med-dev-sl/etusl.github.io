import React, { useEffect, useState } from 'react';
import '../About.css';

export default function OverView() {
	const [overviewData, setOverviewData] = useState(null);
	const [loading, setLoading] = useState(true);
	const [error, setError] = useState(null);

	useEffect(() => {
		const fetchOverview = async () => {
			try {
				// Fetch the first/main about overview (assumes admin creates one)
				const response = await fetch('/api/about-overviews/');
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

	if (loading) return <div className="overview-loading">Loading...</div>;
	if (error) return <div className="overview-error">Error: {error}</div>;
	if (!overviewData) return <div className="overview-empty">No overview data available</div>;

	return (
		<>
			{/* Profile Section: Brief + Statistics */}
			<section className="overview-profile" aria-label="University Profile">
				<div className="overview-container">
					<div className="profile-brief">
						<h2 className="profile-title">Profile</h2>
						<div className="profile-text" dangerouslySetInnerHTML={{ __html: overviewData.brief }} />
					</div>
					<div className="profile-statistics">
						{overviewData.stat_items && overviewData.stat_items.length > 0 ? (
							overviewData.stat_items.map((stat) => (
								<div key={stat.id} className="stat-card">
									<div className="stat-value">{stat.value}</div>
									<div className="stat-label">{stat.label}</div>
								</div>
							))
						) : (
							<p>No statistics available</p>
						)}
					</div>
				</div>
			</section>

			{/* Campuses Section */}
			{overviewData.campuses && overviewData.campuses.length > 0 && (
				<section className="overview-campuses" aria-label="Our Campuses">
					<div className="overview-container">
						<h2 className="section-title">Our Campuses</h2>
						<div className="campuses-grid">
							{overviewData.campuses.map((campus) => (
								<div key={campus.id} className="campus-card">
									{campus.image && (
										<div className="campus-image-wrapper">
											<img src={campus.image} alt={campus.name} className="campus-image" />
											<div className="campus-overlay">
												<h3 className="campus-name">{campus.name}</h3>
											</div>
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
				<section className="overview-content" aria-label="Overview Content">
					<div className="overview-container">
						<div className="content-text" dangerouslySetInnerHTML={{ __html: overviewData.content }} />
					</div>
				</section>
			)}

			{/* Images Gallery Section */}
			{overviewData.images && overviewData.images.length > 0 && (
				<section className="overview-gallery" aria-label="University Gallery">
					<div className="overview-container">
						<div className="images-grid">
							{overviewData.images.map((img) => (
								<div key={img.id} className="gallery-item">
									{img.image && (
										<img src={img.image} alt={img.caption || 'Gallery'} className="gallery-image" />
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

