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
        — Destination: propsmartrealty@gmail.com
     ============================================= */
  const forms = document.querySelectorAll('.sovereign-form-logic');
  const modal = document.getElementById('enquiryModal');
  const closeModal = document.getElementById('closeModal');
  
  // Modal Trigger Logic
  document.querySelectorAll('.btn-modal, .cta-pill, .btn-primary, .btn-secondary, .nav-links a, .ribbon-cta').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const text = (btn.innerText || btn.textContent).toLowerCase();
      const modalHeader = modal?.querySelector('.modal-header h3');
      const modalDesc   = modal?.querySelector('.modal-header p');
      
      // Target specific high-intent phrases
      if (text.includes('enquire') || text.includes('visit') || text.includes('price') || text.includes('access') || text.includes('roi') || text.includes('calc')) {
        e.preventDefault();
        
        // Contextual Header Update
        if (modalHeader) {
          if (text.includes('roi') || text.includes('growth')) {
            modalHeader.innerHTML = 'Request <span class="gold">ROI Analysis</span>';
            modalDesc.innerText   = 'Unlock the complete market whitepaper and capital appreciation projection.';
          } else if (text.includes('price')) {
            modalHeader.innerHTML = 'Get <span class="gold">Price List</span>';
            modalDesc.innerText   = 'Receive the latest inventory status and pre-launch pricing directly on WhatsApp.';
          } else {
            modalHeader.innerHTML = 'Unlock <span class="gold">Privilege Access</span>';
            modalDesc.innerText   = 'Enter your details to receive the official brochure and priority site visit slots.';
          }
        }

        modal.classList.add('open');
        trackEvent('Engagement', 'Modal Opened', text.trim());
      }
    });
  });

  closeModal?.addEventListener('click', () => modal.classList.remove('open'));
  window.addEventListener('click', (e) => { if (e.target === modal) modal.classList.remove('open'); });

  forms.forEach(form => {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      const currentBtn = form.querySelector('.submit-btn');
      const currentBtnText = currentBtn.querySelector('span');

      // --- Validation ---
      const name   = form.querySelector('input[name="name"]');
      const phone  = form.querySelector('input[name="phone"]');
      const config = form.querySelector('select[name="config"]');
      let valid = true;

      [name, phone, config].forEach(el => el.classList.remove('error'));

      if (!name.value.trim()) { name.classList.add('error'); valid = false; }
      if (!phone.value.trim() || !/^[0-9]{10}$/.test(phone.value.trim())) {
        phone.classList.add('error'); valid = false;
      }

      if (!valid) {
        shake(currentBtn);
        return;
      }

      // --- Loading State ---
      currentBtn.disabled = true;
      const originalBtnText = currentBtnText.textContent;
      currentBtnText.textContent = '⏳ Dispatching...';

      // UTM/Source Data
      const urlParams = new URLSearchParams(window.location.search);
      const data = {
        name:    name.value.trim(),
        phone:   phone.value.trim(),
        email:   form.querySelector('input[name="email"]')?.value.trim() || 'N/A',
        config:  config.value,
        source:  urlParams.get('utm_source') || 'Direct',
        campaign: urlParams.get('utm_campaign') || 'Direct_Organic',
        page:    window.location.pathname,
        ts:      new Date().toLocaleString()
      };

      // Persist to local "Sovereign Vault"
      persistLead(data);

      // --- Lead Relay (Email Notification via Web3Forms) ---
      // Destination: propsmartrealty@gmail.com
      const leadData = {
        access_key: 'b28972bc-8e15-4fe5-86b7-82b12ee0e82b',
        subject: `New Lead: ${data.name} - Krisala Aventis`,
        from_name: 'Krisala Aventis Live Portal',
        ...data
      };

      fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
        body: JSON.stringify(leadData)
      }).then(response => {
        if (response.ok) {
          console.log('[Krisala Aventis] Lead relayed to Web3Forms successfully ✅');
        }
      }).catch(err => console.warn('[Krisala Aventis] Lead relay failed:', err));

      // --- Success Execution ---
      setTimeout(() => {
        trackEvent('Conversion', 'Enquiry Form Submission', data.config);
        
        // WhatsApp Dispatch
        const waMsg = buildWhatsAppMessage(data);
        const waUrl = `https://api.whatsapp.com/send?phone=917744009295&text=${waMsg}`;
        window.open(waUrl, '_blank');

        // UI Reset
        showSuccess(currentBtn, currentBtnText);
        form.reset();
        
        // Close modal if open
        setTimeout(() => modal.classList.remove('open'), 2000);
      }, 800);
    });
  });

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

  function showSuccess(btn, btnText) {
    btn.disabled = false;
    btn.style.background = 'var(--clr-wa)';
    btn.style.color = '#fff';
    btnText.textContent = '🏠 Access Granted! WhatsApp Opening...';
    
    setTimeout(() => {
      btn.style.background = '';
      btn.style.color = '';
      btnText.textContent = 'Get Priority Callback 🏠';
    }, 5000);
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
     10. ANALYTICS & EVENT TRACKING (dataLayer)
     ============================================= */
  function trackEvent(category, action, label) {
    if (window.dataLayer) {
      window.dataLayer.push({
        'event': 'ka_engagement',
        'event_category': category,
        'event_action': action,
        'event_label': label
      });
      console.log(`[Analytics] Tracked: ${category} | ${action} | ${label}`);
    }
  }

  // Track WhatsApp Clicks
  document.getElementById('waFab')?.addEventListener('click', () => {
    trackEvent('Communication', 'WhatsApp Click', 'Floating FAB');
  });

  // Track CTA Button Clicks
  document.querySelectorAll('.btn-primary, .btn-secondary, .cta-pill, .ribbon-cta').forEach(btn => {
    btn.addEventListener('click', () => {
      const text = btn.innerText || btn.textContent;
      trackEvent('Engagement', 'Button Click', text.trim());
    });
  });

  /* =============================================
     11. INJECT SHAKE KEYFRAME DYNAMICALLY
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

  const connStyle = document.createElement('style');
  connStyle.textContent = `
    .share-btn-fp { margin-top: 1rem; display: inline-flex; align-items: center; gap: 8px; font-size: 0.85rem; color: var(--clr-gold); cursor: pointer; opacity: 0.8; transition: 0.3s; }
    .share-btn-fp:hover { opacity: 1; transform: translateX(5px); }
  `;
  document.head.appendChild(connStyle);

  document.querySelectorAll('.fp-details').forEach(details => {
    const shareBtn = document.createElement('div');
    shareBtn.className = 'share-btn-fp';
    shareBtn.innerHTML = '<span>📲 Share Layout</span>';
    shareBtn.onclick = () => {
      const bhk = details.querySelector('h3')?.innerText || '2/3 BHK';
      const msg = encodeURIComponent(`Check out this ${bhk} layout at Krisala Aventis Tathawade! It looks perfect. \n\nView here: ${window.location.href}`);
      window.open(`https://api.whatsapp.com/send?text=${msg}`, '_blank');
    };
    details.appendChild(shareBtn);
  });

  console.log('[Krisala Aventis] Sovereign Intelligence v2.0 — ACTIVE ✅');
})();
