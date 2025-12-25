import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import TopHeader from './components/TopHeader';
import MainHeader from './components/MainHeader';
import Footer from './components/Footer';
import Home from './pages/Home';
import AboutOverview from './pages/AboutOverview';
import AboutHistory from './pages/AboutHistory';
import AboutVisionMission from './pages/AboutVisionMission';
import AboutLeadership from './pages/AboutLeadership';
import AboutAffiliates from './pages/AboutAffiliates';
import AboutStrategicPlan from './pages/AboutStrategicPlan';
import AboutPolicies from './pages/AboutPolicies';
import AcademicsOverview from './pages/AcademicsOverview';
import Faculties from './pages/Faculties';
import Programmes from './pages/Programmes';
import AcademicCalendar from './pages/AcademicCalendar';
import Library from './pages/Library';

function App() {
  return (
    <BrowserRouter>
      <TopHeader />
      <MainHeader />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about/overview" element={<AboutOverview />} />
        <Route path="/about/history" element={<AboutHistory />} />
        <Route path="/about/vision-mission" element={<AboutVisionMission />} />
        <Route path="/about/leadership" element={<AboutLeadership />} />
        <Route path="/about/affiliates" element={<AboutAffiliates />} />
        <Route path="/about/strategic-plan" element={<AboutStrategicPlan />} />
        <Route path="/about/policies" element={<AboutPolicies />} />
        <Route path="/academics/overview" element={<AcademicsOverview />} />
        <Route path="/academics/faculties" element={<Faculties />} />
        <Route path="/academics/programmes" element={<Programmes />} />
        <Route path="/academics/calendar" element={<AcademicCalendar />} />
        <Route path="/academics/library" element={<Library />} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
