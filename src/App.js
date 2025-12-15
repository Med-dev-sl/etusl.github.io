import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import TopHeader from './components/TopHeader';
import MainHeader from './components/MainHeader';
import Home from './pages/Home';

function App() {
  return (
    <BrowserRouter>
      <TopHeader />
      <MainHeader />
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
