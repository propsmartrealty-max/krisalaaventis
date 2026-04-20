/* Krisala Aventis — Sovereign Intelligence Script v2.0 */
(function () {
  'use strict';

  /* =============================================
     1. SCROLL REVEAL
     ============================================= */
  const reveals = document.querySelectorAll('.reveal');
  const revealObs = new IntersectionObserver((entries) => {
    entries.forEach((e, i) => {
      if (e.isIntersecting) {
        setTimeout(() => e.target.classList.add('visible'), i * 80);
        revealObs.unobserve(e.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -60px 0px' });
  reveals.forEach(el => revealObs.observe(el));

  /* =============================================
     2. NAVBAR — SCROLL + HAMBURGER
     ============================================= */
  const nav      = document.getElementById('mainNav');
  const hamburger = document.getElementById('hamburger');
  const navLinks  = document.getElementById('navLinks');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 80) {
      nav.classList.add('scrolled');
    } else {
      nav.classList.remove('scrolled');
    }
  });

  hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('open');
    hamburger.textContent = navLinks.classList.contains('open') ? '✕' : '☰';
  });

  // Close mobile nav on link click
  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('open');
      hamburger.textContent = '☰';
    });
  });

  /* =============================================
     3. FLOOR PLAN TABS
     ============================================= */
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabs     = document.querySelectorAll('.fp-tab');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.dataset.tab;

      tabBtns.forEach(b => b.classList.remove('active'));
      tabs.forEach(t => t.classList.remove('active'));

      btn.classList.add('active');
      document.getElementById(target).classList.add('active');

      // Re-trigger reveals in new tab
      document.getElementById(target).querySelectorAll('.reveal').forEach(el => {
        el.classList.remove('visible');
        setTimeout(() => el.classList.add('visible'), 100);
      });
    });
  });

  /* =============================================
     4. SMOOTH SCROLL FOR ANCHOR LINKS
     ============================================= */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const id = anchor.getAttribute('href');
      if (id === '#') return;
      const target = document.querySelector(id);
      if (target) {
        e.preventDefault();
        const offset = 90;
        const top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  /* =============================================
     5. STICKY RIBBON BANISHMENT ON SCROLL
     ============================================= */
  const ribbon = document.getElementById('stickyRibbon');
  let ribbonVisible = true;
  window.addEventListener('scroll', () => {
    if (window.scrollY > 200 && ribbonVisible) {
      ribbon.style.transform = 'translateY(-100%)';
      nav.style.top = '10px';
      ribbonVisible = false;
    } else if (window.scrollY <= 200 && !ribbonVisible) {
      ribbon.style.transform = 'translateY(0)';
      nav.style.top = '44px';
      ribbonVisible = true;
    }
  });
  ribbon.style.transition = 'transform 0.4s cubic-bezier(0.4,0,0.2,1)';
  nav.style.transition     = 'top 0.4s cubic-bezier(0.4,0,0.2,1), background 0.4s, border 0.4s';

  /* =============================================
     6. MARQUEE DUPLICATE (for seamless loop)
     ============================================= */
  const track = document.querySelector('.stats-track');
  if (track) {
    track.innerHTML += track.innerHTML;
  }

  /* =============================================
     7. SOVEREIGN ENQUIRY PIPELINE
        — Dual Dispatch: WhatsApp + Thank You State
     ============================================= */
  const form    = document.getElementById('sovereign-form');
  const btnEl   = document.getElementById('submitBtn');
  const btnText = document.getElementById('btnText');

  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      // --- Validation ---
      const name   = document.getElementById('name');
      const phone  = document.getElementById('phone');
      const config = document.getElementById('config');
      let valid = true;

      [name, phone, config].forEach(el => el.classList.remove('error'));

      if (!name.value.trim()) { name.classList.add('error'); valid = false; }
      if (!phone.value.trim() || !/^[0-9]{10}$/.test(phone.value.trim())) {
        phone.classList.add('error'); valid = false;
      }
      if (!config.value) { config.classList.add('error'); valid = false; }

      if (!valid) {
        shake(btnEl);
        return;
      }

      // --- Loading State ---
      btnEl.disabled = true;
      btnText.textContent = '⏳ Dispatching...';

      // UTM Parameter Extraction
      const urlParams = new URLSearchParams(window.location.search);
      const utmParams = {
        source: urlParams.get('utm_source') || 'Direct',
        medium: urlParams.get('utm_medium') || 'None',
        campaign: urlParams.get('utm_campaign') || 'None'
      };

      // Collect form data
      const data = {
        name:    name.value.trim(),
        phone:   phone.value.trim(),
        email:   document.getElementById('email').value.trim(),
        config:  config.value,
        budget:  document.getElementById('budget').value,
        message: document.getElementById('message').value.trim(),
        utm:     utmParams,
        ts:      new Date().toISOString()
      };

      // Persist to localStorage (Sovereign Vault)
      persistLead(data);

      // --- WhatsApp Dispatch ---
      const waMsg = buildWhatsAppMessage(data);
      const waUrl = `https://api.whatsapp.com/send?phone=919172174141&text=${waMsg}`;

      setTimeout(() => {
        window.open(waUrl, '_blank');
        showSuccess();
        form.reset();
      }, 900);
    });
  }

  function buildWhatsAppMessage(d) {
    let msg = `Hello Krisala Aventis Team! 🏢%0A%0A`;
    msg += `I am interested in Krisala Aventis, Tathawade.%0A%0A`;
    msg += `*My Details:*%0A`;
    msg += `• Name: ${d.name}%0A`;
    msg += `• Mobile: ${d.phone}%0A`;
    if (d.email) msg += `• Email: ${d.email}%0A`;
    msg += `• Configuration: ${d.config}%0A`;
    if (d.budget) msg += `• Budget: ${d.budget}%0A`;
    if (d.message) msg += `• Query: ${d.message}%0A%0A`;
    
    // Add Tracking Metadata
    if (d.utm && (d.utm.source !== 'Direct' || d.utm.campaign !== 'None')) {
      msg += `*Source Data:*%0A`;
      msg += `• Source: ${d.utm.source}%0A`;
      msg += `• Campaign: ${d.utm.campaign}%0A%0A`;
    }

    msg += `Please send me the brochure, floor plans, and schedule a site visit. Thank you!`;
    return msg;
  }

  function persistLead(data) {
    try {
      const vault = JSON.parse(localStorage.getItem('ka_sovereign_vault') || '[]');
      vault.push(data);
      localStorage.setItem('ka_sovereign_vault', JSON.stringify(vault));
      console.log('[Krisala Aventis] Lead persisted to Sovereign Vault:', data);
    } catch (err) {
      console.warn('[Krisala Aventis] Vault write failed:', err);
    }
  }

  function showSuccess() {
    btnEl.disabled = false;
    btnEl.style.background = 'var(--clr-gold)';
    btnEl.style.color = '#000';
    btnText.textContent = '🏠 Privilege Access Granted!';
    
    setTimeout(() => {
      btnEl.style.background = '';
      btnEl.style.color = '';
      btnText.textContent = 'Unlock Privilege Access 🏠';
    }, 6000);
  }

  function shake(el) {
    el.style.animation = 'none';
    requestAnimationFrame(() => {
      el.style.animation = 'shake 0.4s ease';
    });
  }

  /* =============================================
     8. ACTIVE NAV LINK ON SCROLL (highlight)
     ============================================= */
  const sections = document.querySelectorAll('section[id]');
  const navAnchors = document.querySelectorAll('.nav-links a[href^="#"]');

  const sectionObs = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        const id = e.target.id;
        navAnchors.forEach(a => {
          a.style.color = a.getAttribute('href') === `#${id}`
            ? 'var(--clr-gold)' : '';
        });
      }
    });
  }, { threshold: 0.4 });

  sections.forEach(s => sectionObs.observe(s));

  /* =============================================
     9. BACK TO TOP ON LOGO CLICK
     ============================================= */
  document.querySelector('.logo')?.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  /* =============================================
     10. INJECT SHAKE KEYFRAME DYNAMICALLY
     ============================================= */
  const shakeStyle = document.createElement('style');
  shakeStyle.textContent = `
    @keyframes shake {
      0%, 100% { transform: translateX(0); }
      20%       { transform: translateX(-8px); }
      40%       { transform: translateX(8px); }
      60%       { transform: translateX(-5px); }
      80%       { transform: translateX(5px); }
    }
  `;
  document.head.appendChild(shakeStyle);

  console.log('[Krisala Aventis] Sovereign Intelligence v2.0 — ACTIVE ✅');
})();
