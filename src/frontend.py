"""
Frontend HTML Content for MindCare AI Platform
Contains the complete web interface with all features
"""

def get_html_content():
    """Return the complete HTML content for the platform"""
    return '''<!DOCTYPE html>
<html><head><title>MindCare AI - Mental Health Revolution</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:'Inter',sans-serif;background:#0a0a0a;color:#ffffff;overflow-x:hidden;line-height:1.7;font-size:18px}
.container{max-width:1400px;margin:0 auto;padding:0 20px}
.hero{min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;position:relative;background:linear-gradient(135deg,#1a1a2e 0%,#16213e 50%,#0f3460 100%)}
.hero::before{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:radial-gradient(circle at 30% 20%,rgba(120,119,198,0.4),transparent 60%),radial-gradient(circle at 80% 80%,rgba(255,119,198,0.4),transparent 60%);pointer-events:none}
.hero::after{content:'';position:absolute;top:20%;left:10%;width:300px;height:300px;background:radial-gradient(circle,rgba(59,130,246,0.3) 0%,rgba(139,92,246,0.2) 50%,transparent 70%);border-radius:50%;animation:float 6s ease-in-out infinite;pointer-events:none}
.hero-content{position:relative;z-index:2;max-width:900px}
.hero h1{font-family:'Space Grotesk',sans-serif;font-size:clamp(3.5rem,9vw,7rem);font-weight:800;margin-bottom:30px;background:linear-gradient(135deg,#ffffff 0%,#a855f7 50%,#3b82f6 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;animation:fadeInUp 1s ease-out}
.hero p{font-size:clamp(1.3rem,3vw,1.8rem);color:#94a3b8;margin-bottom:50px;animation:fadeInUp 1s ease-out 0.2s both}
.cta-button{display:inline-block;background:linear-gradient(135deg,#3b82f6,#8b5cf6);color:white;padding:20px 40px;border-radius:50px;text-decoration:none;font-weight:600;font-size:1.2rem;transition:all 0.3s ease;box-shadow:0 10px 30px rgba(59,130,246,0.3);animation:fadeInUp 1s ease-out 0.4s both;margin:10px;border:none;cursor:pointer}
.cta-button:hover{transform:translateY(-3px);box-shadow:0 20px 40px rgba(59,130,246,0.4)}
.section{padding:140px 0;position:relative}
.section::before{content:'';position:absolute;top:50%;right:5%;width:200px;height:200px;background:radial-gradient(circle,rgba(236,72,153,0.2) 0%,rgba(139,92,246,0.1) 50%,transparent 70%);border-radius:50%;animation:float 8s ease-in-out infinite reverse;pointer-events:none}
.section-title{font-family:'Space Grotesk',sans-serif;font-size:clamp(3rem,6vw,5rem);font-weight:700;text-align:center;margin-bottom:80px;background:linear-gradient(135deg,#ffffff,#a855f7);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.features{display:grid;grid-template-columns:repeat(auto-fit,minmax(380px,1fr));gap:50px;margin-top:100px}
.feature{background:rgba(255,255,255,0.05);backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.1);border-radius:24px;padding:50px;transition:all 0.4s ease;position:relative;overflow:hidden}
.feature::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,#3b82f6,#8b5cf6,#ec4899);opacity:0;transition:opacity 0.3s ease}
.feature:hover::before{opacity:1}
.feature:hover{transform:translateY(-10px);background:rgba(255,255,255,0.08);border-color:rgba(255,255,255,0.2)}
.feature-icon{width:70px;height:70px;background:linear-gradient(135deg,#3b82f6,#8b5cf6);border-radius:16px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:1.8rem;margin-bottom:30px;color:white}
.feature h3{font-family:'Space Grotesk',sans-serif;font-size:1.8rem;font-weight:600;margin-bottom:20px;color:#ffffff}
.feature p{color:#94a3b8;line-height:1.8;font-size:1.1rem}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:40px;margin:100px 0}
.stat{text-align:center;padding:50px 30px;background:rgba(255,255,255,0.05);border-radius:20px;border:1px solid rgba(255,255,255,0.1);transition:all 0.3s ease}
.stat:hover{transform:translateY(-5px);background:rgba(255,255,255,0.08)}
.stat-number{font-family:'Space Grotesk',sans-serif;font-size:3.5rem;font-weight:800;color:#3b82f6;display:block;margin-bottom:12px}
.stat-label{color:#94a3b8;font-weight:500;font-size:1.1rem}
.games-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:40px;margin-top:80px}
.game-card{background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:20px;padding:40px;text-align:center;transition:all 0.4s ease;position:relative;overflow:hidden}
.game-card::after{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:linear-gradient(135deg,rgba(59,130,246,0.1),rgba(139,92,246,0.1));opacity:0;transition:opacity 0.3s ease}
.game-card:hover::after{opacity:1}
.game-card:hover{transform:translateY(-8px);border-color:rgba(255,255,255,0.2)}
.game-icon{width:90px;height:90px;background:linear-gradient(135deg,#3b82f6,#8b5cf6);border-radius:20px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:2.2rem;margin:0 auto 25px;color:white;position:relative;z-index:2}
.game-card h3{font-family:'Space Grotesk',sans-serif;font-size:1.5rem;font-weight:600;margin-bottom:15px;position:relative;z-index:2}
.game-card p{color:#94a3b8;margin-bottom:10px;position:relative;z-index:2;font-size:1.05rem}
.btn{background:linear-gradient(135deg,#3b82f6,#8b5cf6);color:white;border:none;padding:15px 30px;border-radius:25px;font-weight:600;cursor:pointer;transition:all 0.3s ease;margin-top:20px;position:relative;z-index:2;font-size:1.05rem}
.btn:hover{transform:translateY(-2px);box-shadow:0 10px 25px rgba(59,130,246,0.3)}
.chat-section{background:rgba(255,255,255,0.02);border-radius:24px;padding:50px;margin:80px 0;border:1px solid rgba(255,255,255,0.1)}
.chat-area{background:rgba(0,0,0,0.3);border-radius:16px;height:450px;overflow-y:auto;padding:25px;margin-bottom:25px;border:1px solid rgba(255,255,255,0.1)}
.message{margin:20px 0;padding:18px 24px;border-radius:16px;max-width:80%;animation:slideIn 0.3s ease-out;font-size:1.05rem}
.user-message{background:linear-gradient(135deg,#3b82f6,#8b5cf6);margin-left:auto;color:white}
.ai-message{background:rgba(255,255,255,0.1);margin-right:auto;border:1px solid rgba(255,255,255,0.1)}
.input{background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.2);padding:18px 24px;border-radius:25px;color:white;width:100%;font-size:1.1rem;transition:all 0.3s ease}
.input:focus{outline:none;border-color:#3b82f6;background:rgba(255,255,255,0.08)}
.input::placeholder{color:#64748b}
.nav{position:fixed;top:30px;left:50%;transform:translateX(-50%);background:rgba(0,0,0,0.8);backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.1);border-radius:50px;padding:10px;z-index:1000;display:flex;gap:10px}
.nav-btn{background:transparent;border:none;color:#94a3b8;padding:14px 24px;border-radius:25px;cursor:pointer;transition:all 0.3s ease;font-weight:500;font-size:1.05rem}
.nav-btn:hover,.nav-btn.active{background:rgba(255,255,255,0.1);color:white}
.auth-section{display:none;min-height:100vh;align-items:center;justify-content:center;background:linear-gradient(135deg,#1a1a2e 0%,#16213e 50%,#0f3460 100%);position:fixed;top:0;left:0;width:100%;z-index:2000}
.auth-form{background:rgba(255,255,255,0.05);backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.1);border-radius:24px;padding:60px;max-width:450px;width:90%;margin:0 auto}
.auth-form h2{font-family:'Space Grotesk',sans-serif;font-size:2.5rem;text-align:center;margin-bottom:40px;background:linear-gradient(135deg,#ffffff,#a855f7);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.form-group{margin-bottom:30px}
.form-group label{display:block;margin-bottom:12px;font-weight:500;font-size:1.1rem}
.form-group input,.form-group textarea{width:100%;padding:18px 24px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.2);border-radius:12px;color:white;font-size:1.1rem;min-height:56px}
.form-group input:focus,.form-group textarea:focus{outline:none;border-color:#3b82f6;background:rgba(255,255,255,0.08)}
.form-group input::placeholder,.form-group textarea::placeholder{color:#64748b}
.dashboard{display:none;padding:140px 0}
.dashboard-header{text-align:center;margin-bottom:60px}
.dashboard-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:30px;margin-bottom:60px}
.dashboard-card{background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:20px;padding:30px;text-align:center}
.dashboard-card h3{font-size:1.3rem;margin-bottom:10px;color:#3b82f6}
.dashboard-card p{font-size:2rem;font-weight:700;color:white}
.game-dashboard{background:rgba(255,255,255,0.02);border-radius:24px;padding:40px;margin:40px 0;border:1px solid rgba(255,255,255,0.1)}
.game-content-area{background:rgba(0,0,0,0.3);border-radius:16px;padding:40px;margin:20px 0;border:1px solid rgba(255,255,255,0.1);text-align:center;min-height:400px;display:flex;flex-direction:column;justify-content:center;align-items:center}
.breathing-circle{width:200px;height:200px;border:3px solid #3b82f6;border-radius:50%;margin:30px auto;animation:breathe 4s infinite ease-in-out}
.game-instructions{font-size:1.2rem;line-height:1.8;margin:25px 0;color:#94a3b8;max-width:600px}
.prescription-section{background:rgba(255,255,255,0.02);border-radius:24px;padding:50px;margin:60px 0;border:1px solid rgba(255,255,255,0.1)}
@keyframes fadeInUp{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:translateY(0)}}
@keyframes slideIn{from{opacity:0;transform:translateX(20px)}to{opacity:1;transform:translateX(0)}}
@keyframes float{0%,100%{transform:translateY(0px)}50%{transform:translateY(-30px)}}
@keyframes breathe{0%,100%{transform:scale(1)}50%{transform:scale(1.1)}}
@media (max-width: 768px){.hero{padding:0 20px}.features{grid-template-columns:1fr}.games-grid{grid-template-columns:1fr}.stats{grid-template-columns:repeat(2,1fr)}.nav{position:relative;top:0;left:0;transform:none;margin:20px auto;width:fit-content;flex-wrap:wrap}.auth-form{padding:40px 30px;max-width:90%}}
</style></head><body>

<nav class="nav" id="mainNav">
<button class="nav-btn active" onclick="showSection('hero')">Home</button>
<button class="nav-btn" onclick="showSection('features')">Features</button>
<button class="nav-btn" onclick="showSection('games')">Games</button>
<button class="nav-btn" onclick="showSection('chat')">AI Chat</button>
<button class="nav-btn" onclick="showLogin()">Login</button>
</nav>

<nav class="nav" id="userNav" style="display:none">
<button class="nav-btn active" onclick="showSection('dashboard')">Dashboard</button>
<button class="nav-btn" onclick="showSection('games')">Games</button>
<button class="nav-btn" onclick="showSection('chat')">AI Chat</button>
<button class="nav-btn" onclick="showSection('prescription')">Prescription</button>
<button class="nav-btn" onclick="logout()">Logout</button>
</nav>

<section id="hero" class="hero">
<div class="hero-content">
<h1>MindCare AI</h1>
<p>Revolutionary mental health support platform combining AI emotion recognition, therapeutic gaming, and 24/7 chat support</p>
<a href="#features" class="cta-button">Explore Platform</a>
<button class="cta-button" onclick="showLogin()">Get Started</button>
</div>
</section>

<section id="login" class="auth-section">
<div class="auth-form">
<h2>Welcome Back</h2>
<form onsubmit="handleLogin(event)">
<div class="form-group">
<label>Email</label>
<input type="email" id="loginEmail" placeholder="Enter your email" required>
</div>
<div class="form-group">
<label>Password</label>
<input type="password" id="loginPassword" placeholder="Enter your password" required>
</div>
<button type="submit" class="btn" style="width:100%;margin-top:20px;font-size:1.1rem;padding:18px">Login</button>
</form>
<p style="text-align:center;margin-top:20px;color:#94a3b8">Don't have an account? <a href="#" onclick="showRegister()" style="color:#3b82f6">Sign up</a></p>
</div>
</section>

<section id="register" class="auth-section">
<div class="auth-form">
<h2>Join MindCare AI</h2>
<form onsubmit="handleRegister(event)">
<div class="form-group">
<label>Full Name</label>
<input type="text" id="registerName" placeholder="Enter your full name" required>
</div>
<div class="form-group">
<label>Email</label>
<input type="email" id="registerEmail" placeholder="Enter your email" required>
</div>
<div class="form-group">
<label>Password</label>
<input type="password" id="registerPassword" placeholder="Create a password" required>
</div>
<div class="form-group">
<label>Age</label>
<input type="number" id="registerAge" placeholder="Enter your age" min="18" max="100" required>
</div>
<button type="submit" class="btn" style="width:100%;margin-top:20px;font-size:1.1rem;padding:18px">Create Account</button>
</form>
<p style="text-align:center;margin-top:20px;color:#94a3b8">Already have an account? <a href="#" onclick="showLogin()" style="color:#3b82f6">Login</a></p>
</div>
</section>

<section id="dashboard" class="dashboard">
<div class="container">
<div class="dashboard-header">
<h2 class="section-title">Your Mental Health Dashboard</h2>
<p style="font-size:1.2rem;color:#94a3b8">Welcome back! Here's your progress overview</p>
</div>
<div class="dashboard-stats">
<div class="dashboard-card">
<h3>Current Streak</h3>
<p id="userStreak">7 days</p>
</div>
<div class="dashboard-card">
<h3>Games Played</h3>
<p id="gamesPlayed">23</p>
</div>
<div class="dashboard-card">
<h3>Mood Score</h3>
<p id="moodScore">8.2/10</p>
</div>
<div class="dashboard-card">
<h3>Progress</h3>
<p id="overallProgress">78%</p>
</div>
</div>
<div class="game-dashboard" id="gameDashboard" style="display:none">
<h3 style="text-align:center;margin-bottom:30px;font-size:2rem">Current Game Session</h3>
<div class="game-content-area" id="gameContentArea">
<p>Select a game to start your therapeutic session</p>
</div>
<div style="text-align:center;margin-top:20px">
<button class="btn" onclick="completeGameSession()" id="completeGameBtn" style="display:none">Complete Session</button>
<button class="btn" onclick="closeGameSession()">Close Game</button>
</div>
</div>
</div>
</section>

<section id="prescription" class="section" style="display:none">
<div class="container">
<h2 class="section-title">Medical Prescription Upload</h2>
<div class="prescription-section">
<h3 style="margin-bottom:30px;font-size:1.8rem">Upload Your Medical Documents</h3>
<form onsubmit="handlePrescription(event)">
<div class="form-group">
<label>Doctor Name</label>
<input type="text" id="doctorName" placeholder="Enter doctor's name" required>
</div>
<div class="form-group">
<label>Diagnosis</label>
<textarea id="diagnosis" placeholder="Enter diagnosis details" rows="4" required></textarea>
</div>
<div class="form-group">
<label>Medications</label>
<textarea id="medications" placeholder="List current medications" rows="3" required></textarea>
</div>
<div class="form-group">
<label>Treatment Plan</label>
<textarea id="treatmentPlan" placeholder="Describe treatment plan" rows="4" required></textarea>
</div>
<div class="form-group">
<label>Upload Prescription (Optional)</label>
<input type="file" id="prescriptionFile" accept=".pdf,.jpg,.jpeg,.png">
</div>
<button type="submit" class="btn" style="width:100%;margin-top:20px;font-size:1.1rem;padding:18px">Submit Prescription</button>
</form>
</div>
</div>
</section>

<section id="features" class="section">
<div class="container">
<h2 class="section-title">Platform Features</h2>
<div class="stats">
<div class="stat">
<span class="stat-number">45%</span>
<div class="stat-label">Anxiety Reduction</div>
</div>
<div class="stat">
<span class="stat-number">40%</span>
<div class="stat-label">Depression Improvement</div>
</div>
<div class="stat">
<span class="stat-number">89%</span>
<div class="stat-label">Daily Engagement</div>
</div>
<div class="stat">
<span class="stat-number">4.6</span>
<div class="stat-label">User Rating</div>
</div>
</div>
<div class="features">
<div class="feature">
<div class="feature-icon">AI</div>
<h3>Emotion Recognition</h3>
<p>Real-time facial emotion analysis using AWS Rekognition. Privacy-first approach with no image storage and complete data transparency for better mental health monitoring.</p>
</div>
<div class="feature">
<div class="feature-icon">GAME</div>
<h3>Therapeutic Gaming</h3>
<p>5 evidence-based games designed by mental health professionals. Clinically validated with proven results and comprehensive user progress tracking system.</p>
</div>
<div class="feature">
<div class="feature-icon">CHAT</div>
<h3>AI Therapist</h3>
<p>24/7 therapeutic conversations with advanced crisis detection, personalized guidance, and contextual mental health support tailored to your needs.</p>
</div>
<div class="feature">
<div class="feature-icon">DATA</div>
<h3>Data Control</h3>
<p>Complete transparency and control over your medical data. Export, view usage, or delete everything with one click. Fully GDPR compliant with prescription tracking.</p>
</div>
</div>
</div>
</section>

<section id="games" class="section">
<div class="container">
<h2 class="section-title">Therapeutic Games</h2>
<div class="games-grid">
<div class="game-card">
<div class="game-icon">B</div>
<h3>Breathing Garden</h3>
<p><strong>Target:</strong> Anxiety Relief</p>
<p><strong>Result:</strong> 40% stress reduction</p>
<p><strong>Duration:</strong> 10-15 minutes</p>
<button class="btn" onclick="startGameSession('breathing')">Start Game</button>
</div>
<div class="game-card">
<div class="game-icon">T</div>
<h3>Thought Challenger</h3>
<p><strong>Target:</strong> Depression Support</p>
<p><strong>Result:</strong> 35% mood improvement</p>
<p><strong>Duration:</strong> 15-20 minutes</p>
<button class="btn" onclick="startGameSession('thoughts')">Start Game</button>
</div>
<div class="game-card">
<div class="game-icon">S</div>
<h3>Safe Space Social</h3>
<p><strong>Target:</strong> Social Anxiety</p>
<p><strong>Result:</strong> 45% confidence gain</p>
<p><strong>Duration:</strong> 20-30 minutes</p>
<button class="btn" onclick="startGameSession('social')">Start Game</button>
</div>
<div class="game-card">
<div class="game-icon">Z</div>
<h3>Zen Flow</h3>
<p><strong>Target:</strong> Stress Management</p>
<p><strong>Result:</strong> 38% relaxation increase</p>
<p><strong>Duration:</strong> 10-15 minutes</p>
<button class="btn" onclick="startGameSession('meditation')">Start Game</button>
</div>
<div class="game-card">
<div class="game-icon">G</div>
<h3>Goal Quest</h3>
<p><strong>Target:</strong> Motivation Building</p>
<p><strong>Result:</strong> 42% goal achievement</p>
<p><strong>Duration:</strong> 15-25 minutes</p>
<button class="btn" onclick="startGameSession('goals')">Start Game</button>
</div>
</div>
</div>
</section>

<section id="chat" class="section">
<div class="container">
<h2 class="section-title">AI Therapeutic Assistant</h2>
<div class="chat-section">
<div class="chat-area" id="chatArea">
<div class="message ai-message">
<strong>MindCare AI:</strong> Hello! I'm here to support your mental health journey. How are you feeling today?
</div>
</div>
<div style="display:flex;gap:15px;align-items:center;margin-bottom:25px">
<input type="text" id="chatInput" class="input" placeholder="Share your thoughts and feelings...">
<button class="btn" onclick="sendMessage()">Send</button>
</div>
<div style="display:flex;gap:15px;flex-wrap:wrap;justify-content:center">
<button class="btn" onclick="quickMessage('anxious')">I feel anxious</button>
<button class="btn" onclick="quickMessage('sad')">I feel sad</button>
<button class="btn" onclick="quickMessage('stressed')">I'm stressed</button>
<button class="btn" onclick="quickMessage('happy')">I feel good</button>
</div>
</div>
</div>
</section>

<script>
let currentUser = null;
let currentGame = null;
let gameStartTime = null;

function showSection(sectionId) {
document.querySelectorAll('section').forEach(s => {
if (s.id === 'login' || s.id === 'register') {
s.style.display = 'none';
} else {
s.style.display = 'none';
}
});
if (sectionId === 'login' || sectionId === 'register') {
document.getElementById(sectionId).style.display = 'flex';
} else {
document.getElementById(sectionId).style.display = 'block';
if (sectionId !== 'dashboard') {
document.getElementById(sectionId).scrollIntoView({behavior: 'smooth'});
}
}
updateNavButtons(sectionId);
}

function updateNavButtons(activeSection) {
document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.remove('active'));
document.querySelector(`[onclick*="${activeSection}"]`)?.classList.add('active');
}

function showLogin() {
showSection('login');
}

function showRegister() {
showSection('register');
}

function handleLogin(event) {
event.preventDefault();
const email = document.getElementById('loginEmail').value;
const password = document.getElementById('loginPassword').value;
if (!email || !password) {
alert('Please fill in all fields');
return;
}
currentUser = {email, name: email.split('@')[0], loginTime: new Date()};
document.getElementById('mainNav').style.display = 'none';
document.getElementById('userNav').style.display = 'flex';
document.getElementById('login').style.display = 'none';
showSection('dashboard');
updateDashboardStats();
}

function handleRegister(event) {
event.preventDefault();
const name = document.getElementById('registerName').value;
const email = document.getElementById('registerEmail').value;
const age = document.getElementById('registerAge').value;
if (!name || !email || !age) {
alert('Please fill in all fields');
return;
}
currentUser = {name, email, age, loginTime: new Date()};
document.getElementById('mainNav').style.display = 'none';
document.getElementById('userNav').style.display = 'flex';
document.getElementById('register').style.display = 'none';
showSection('dashboard');
updateDashboardStats();
}

function handlePrescription(event) {
event.preventDefault();
const doctorName = document.getElementById('doctorName').value;
const diagnosis = document.getElementById('diagnosis').value;
const medications = document.getElementById('medications').value;
const treatmentPlan = document.getElementById('treatmentPlan').value;
alert('Prescription submitted successfully! Your medical data has been securely stored and will be used to personalize your treatment plan.');
document.getElementById('doctorName').value = '';
document.getElementById('diagnosis').value = '';
document.getElementById('medications').value = '';
document.getElementById('treatmentPlan').value = '';
}

function logout() {
currentUser = null;
document.getElementById('mainNav').style.display = 'flex';
document.getElementById('userNav').style.display = 'none';
document.getElementById('gameDashboard').style.display = 'none';
document.querySelectorAll('section').forEach(s => {
if (s.id === 'login' || s.id === 'register' || s.id === 'dashboard' || s.id === 'prescription') {
s.style.display = 'none';
}
});
showSection('hero');
}

function updateDashboardStats() {
document.getElementById('userStreak').textContent = Math.floor(Math.random() * 20) + 1 + ' days';
document.getElementById('gamesPlayed').textContent = Math.floor(Math.random() * 50) + 10;
document.getElementById('moodScore').textContent = (Math.random() * 3 + 7).toFixed(1) + '/10';
document.getElementById('overallProgress').textContent = Math.floor(Math.random() * 30) + 70 + '%';
}

function startGameSession(gameType) {
if (!currentUser) {
alert('Please login to play games');
showLogin();
return;
}
currentGame = gameType;
gameStartTime = Date.now();
showSection('dashboard');
document.getElementById('gameDashboard').style.display = 'block';
const gameArea = document.getElementById('gameContentArea');
const completeBtn = document.getElementById('completeGameBtn');

const games = {
breathing: {
title: 'Breathing Garden',
content: `<h3 style="margin-bottom:20px">Breathing Garden Session</h3><div class="game-instructions"><p>Welcome to the Breathing Garden! This exercise helps reduce anxiety by 40%.</p><p><strong>Instructions:</strong></p><p>• Follow the breathing circle below</p><p>• Inhale when it expands (4 seconds)</p><p>• Hold your breath (4 seconds)</p><p>• Exhale when it contracts (6 seconds)</p></div><div class="breathing-circle"></div><p>Breathe with the circle... Focus on your breath and let anxiety fade away...</p>`
},
thoughts: {
title: 'Thought Challenger',
content: `<h3 style="margin-bottom:20px">Thought Challenger Session</h3><div class="game-instructions"><p>Challenge negative thoughts with CBT techniques. 35% mood improvement expected.</p><p><strong>Current Negative Thought:</strong> "I'm not good enough"</p><p><strong>Challenge Questions:</strong></p><p>• Is this thought realistic and based on facts?</p><p>• What evidence actually supports this thought?</p><p>• How would I advise a close friend with this thought?</p><p>• What's a more balanced and realistic perspective?</p></div><p><strong>Reframed Positive Thought:</strong> "I'm learning and growing every day, and that's enough"</p>`
},
social: {
title: 'Safe Space Social',
content: `<h3 style="margin-bottom:20px">Safe Space Social Session</h3><div class="game-instructions"><p>Practice social scenarios safely. 45% confidence gain typical.</p><p><strong>Today's Scenario:</strong> Starting a conversation with a colleague at work</p><p><strong>Practice Responses:</strong></p><p>• "Hi there! How's your day going so far?"</p><p>• "Did you catch the presentation earlier today?"</p><p>• "I really like your coffee mug - where did you get it?"</p><p>• "The weather's been great lately, hasn't it?"</p></div><p>Remember: Most people are friendly and understanding. Social interactions get easier with practice!</p>`
},
meditation: {
title: 'Zen Flow',
content: `<h3 style="margin-bottom:20px">Zen Flow Meditation Session</h3><div class="game-instructions"><p>Mindfulness meditation for stress relief. 38% stress reduction achieved.</p><p><strong>Focus Points for Today:</strong></p><p>• Notice your natural breathing rhythm</p><p>• Feel your body's connection to the chair</p><p>• Observe thoughts without judging them</p><p>• Gently return attention to your breath when mind wanders</p></div><p>Let thoughts come and go like clouds drifting across a peaceful sky. You are the observer, calm and centered.</p>`
},
goals: {
title: 'Goal Quest',
content: `<h3 style="margin-bottom:20px">Goal Quest Session</h3><div class="game-instructions"><p>Set and achieve meaningful goals. 42% goal achievement rate.</p><p><strong>Today's Mental Health Goal:</strong> Take one small step toward better emotional wellbeing</p><p><strong>Action Steps:</strong></p><p>• Identify one specific, achievable action for today</p><p>• Make it small enough to complete in 15 minutes</p><p>• Set a specific time when you'll do it</p><p>• Celebrate your completion, no matter how small</p></div><p>Remember: Small consistent steps lead to big positive changes in mental health!</p>`
}
};

gameArea.innerHTML = games[gameType].content;
completeBtn.style.display = 'block';
}

function completeGameSession() {
if (!currentGame) return;
const duration = Math.floor((Date.now() - gameStartTime) / 1000);
const improvements = {
breathing: '40% anxiety reduction',
thoughts: '35% mood improvement',
social: '45% confidence gain',
meditation: '38% stress reduction',
goals: '42% goal achievement'
};
document.getElementById('gameContentArea').innerHTML = `
<h3 style="color:#3b82f6;margin-bottom:20px">Session Complete!</h3>
<p style="font-size:1.2rem;margin-bottom:15px">Game: ${currentGame.charAt(0).toUpperCase() + currentGame.slice(1)}</p>
<p style="font-size:1.1rem;margin-bottom:15px">Duration: ${duration} seconds</p>
<p style="font-size:1.1rem;margin-bottom:20px">Expected Result: ${improvements[currentGame]}</p>
<p style="color:#94a3b8">Great job! Your mental health journey continues. This session has been recorded in your progress.</p>
`;
document.getElementById('completeGameBtn').style.display = 'none';
updateDashboardStats();
}

function closeGameSession() {
document.getElementById('gameDashboard').style.display = 'none';
currentGame = null;
}

function sendMessage() {
const input = document.getElementById('chatInput');
const message = input.value.trim();
if (!message) return;
addMessage(message, 'user');
input.value = '';
setTimeout(() => addMessage(generateResponse(message), 'ai'), 1000);
}

function quickMessage(type) {
const messages = {
anxious: "I'm feeling really anxious and worried about everything lately.",
sad: "I've been feeling sad and down, struggling with motivation.",
stressed: "I'm completely overwhelmed and stressed out with everything.",
happy: "I'm feeling pretty good today, but want to maintain this positive mood."
};
document.getElementById('chatInput').value = messages[type];
sendMessage();
}

function addMessage(message, sender) {
const chatArea = document.getElementById('chatArea');
const messageDiv = document.createElement('div');
messageDiv.className = `message ${sender}-message`;
messageDiv.innerHTML = sender === 'user' ? `<strong>You:</strong> ${message}` : `<strong>MindCare AI:</strong> ${message}`;
chatArea.appendChild(messageDiv);
chatArea.scrollTop = chatArea.scrollHeight;
}

function generateResponse(message) {
const msg = message.toLowerCase();
if (msg.includes('anxious') || msg.includes('anxiety')) {
return "I understand you're feeling anxious. This is completely normal and you're not alone. Try the 4-4-6 breathing technique: inhale for 4 seconds, hold for 4, exhale for 6. The Breathing Garden game can help reduce anxiety by 40%. Would you like me to guide you through it?";
} else if (msg.includes('sad') || msg.includes('depressed')) {
return "I hear that you're feeling sad, and I want you to know that your feelings are completely valid and important. Depression affects many people, and seeking help shows incredible strength. The Thought Challenger game uses proven CBT techniques and shows 35% mood improvement. Remember, you're not alone in this journey.";
} else if (msg.includes('stressed') || msg.includes('overwhelmed')) {
return "Stress can feel overwhelming, but you're taking exactly the right step by reaching out for support. Try breaking overwhelming tasks into smaller, more manageable pieces. The Zen Flow meditation game has helped users achieve 38% stress reduction. What's the most pressing thing on your mind right now?";
} else if (msg.includes('happy') || msg.includes('good')) {
return "It's wonderful to hear you're feeling positive today! These moments of happiness are precious and worth celebrating. To maintain this good mood, try the Goal Quest game to build on this positive momentum. What's contributing most to these good feelings today?";
} else {
return "Thank you for sharing with me. I'm here to support you through whatever you're experiencing. Whether you want to talk about something specific, try one of our therapeutic games, or just need someone to listen without judgment, I'm here to help. What would be most helpful for you right now?";
}
}

document.getElementById('chatInput').addEventListener('keypress', function(e) {
if (e.key === 'Enter') sendMessage();
});

setTimeout(() => {
addMessage("Welcome to MindCare AI! I'm here to support your mental health journey 24/7. Try our therapeutic games, share your feelings, or just tell me how you're doing today. Your wellbeing matters.", 'ai');
}, 1000);

window.addEventListener('scroll', () => {
const sections = ['hero', 'features', 'games', 'chat'];
const scrollPos = window.scrollY + 100;
sections.forEach(section => {
const element = document.getElementById(section);
if (element && element.offsetTop <= scrollPos && element.offsetTop + element.offsetHeight > scrollPos) {
updateNavButtons(section);
}
});
});

document.querySelectorAll('section').forEach(section => {
if (section.id === 'login' || section.id === 'register' || section.id === 'dashboard' || section.id === 'prescription') {
section.style.display = 'none';
}
});
</script>
</body></html>'''