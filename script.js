/**
 * Sri Tirumala Chemical Industries - Premium Interactivity Script
 * Flipkart-style Product Details Showcase Integration
 */

document.addEventListener('DOMContentLoaded', () => {
    
    // ----------------------------------------------------
    // 1. Preloader Fade Out
    // ----------------------------------------------------
    window.addEventListener('load', () => {
        const preloader = document.getElementById('preloader');
        if (preloader) {
            preloader.classList.add('fade-out');
            setTimeout(() => {
                preloader.style.display = 'none';
            }, 500);
        }
    });

    // Preloader Fallback (max 2.5s)
    setTimeout(() => {
        const preloader = document.getElementById('preloader');
        if (preloader && !preloader.classList.contains('fade-out')) {
            preloader.classList.add('fade-out');
            setTimeout(() => {
                preloader.style.display = 'none';
            }, 500);
        }
    }, 2500);

    // ----------------------------------------------------
    // 2. Sticky Header Navbar
    // ----------------------------------------------------
    const header = document.querySelector('.main-header');
    
    const handleScroll = () => {
        if (window.scrollY > 40) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    };
    
    window.addEventListener('scroll', handleScroll);
    handleScroll();

    // ----------------------------------------------------
    // 3. Mobile Nav Drawer Menu Toggle
    // ----------------------------------------------------
    const menuToggle = document.getElementById('mobile-menu-toggle');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    if (menuToggle && navMenu) {
        menuToggle.addEventListener('click', () => {
            menuToggle.classList.toggle('active');
            navMenu.classList.toggle('mobile-open');
            document.body.style.overflow = navMenu.classList.contains('mobile-open') ? 'hidden' : '';
        });

        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                menuToggle.classList.remove('active');
                navMenu.classList.remove('mobile-open');
                document.body.style.overflow = '';
            });
        });
    }

    // ----------------------------------------------------
    // 4. Active Nav Link Tracking on Scroll
    // ----------------------------------------------------
    const sections = document.querySelectorAll('section');

    const trackActiveLink = () => {
        let currentSectionId = 'home';
        const scrollPosition = window.scrollY + 100; // offset header height

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;

            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                currentSectionId = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            const hrefAttr = link.getAttribute('href');
            if (hrefAttr === `#${currentSectionId}` || (currentSectionId === 'home' && hrefAttr === '#home')) {
                link.classList.add('active');
            }
        });
    };

    window.addEventListener('scroll', trackActiveLink);
    trackActiveLink();

    // ----------------------------------------------------
    // 5. Flipkart-Style Interactive Products Data
    // ----------------------------------------------------
    // Note: productModalData has been moved to products-data.js for easier maintenance

    // Modal DOM Nodes
    const productModal = document.getElementById('product-modal');
    const closeProductModalBtn = document.getElementById('modal-close-btn');
    const subProductsPillsContainer = document.getElementById('sub-products-pills');
    const packagingSizePillsContainer = document.getElementById('packaging-size-pills');
    const highlightsListContainer = document.getElementById('product-highlights-list');
    const specsTableBody = document.getElementById('specs-table-body');
    
    const modalProductImg = document.getElementById('modal-product-img');
    const modalCategoryTag = document.getElementById('modal-category-tag');
    const modalProductTitle = document.getElementById('modal-product-title');
    const modalCategoryDesc = document.getElementById('modal-category-desc');
    const modalWhatsappBtn = document.getElementById('modal-whatsapp-btn');
    const modalEmailBtn = document.getElementById('modal-email-btn');

    let activeCategory = null;
    let activeSubProductIndex = 0;
    let activeSizeIndex = 0;

    // ----------------------------------------------------
    // 6. Dynamic Modal Content Rendering
    // ----------------------------------------------------
    const updateModalInquiryButtons = () => {
        const categoryData = productModalData[activeCategory];
        if (!categoryData) return;

        const subProduct = categoryData.subProducts[activeSubProductIndex];
        const selectedSize = subProduct.sizes[activeSizeIndex];

        // 1. WhatsApp Prefilled link
        const waNumber = "919908914524";
        const waMsgText = `Hello Sri Tirumala Chemical Industries, I am interested in purchasing "${subProduct.name}" from your "${categoryData.title}" range.\n\n- Selected Size: ${selectedSize}\n\nPlease share the catalog, pricing, and bulk delivery details.`;
        modalWhatsappBtn.href = `https://wa.me/${waNumber}?text=${encodeURIComponent(waMsgText)}`;

        // 2. Email Prefilled link
        const emailAddress = "k.pr9908914522@gmail.com";
        const emailSubject = `Inquiry: ${subProduct.name} - ${selectedSize}`;
        const emailBody = `Hello Sri Tirumala Chemical Industries Sales Team,\n\nI would like to receive a price quote and technical specification sheets for:\n\nProduct: ${subProduct.name}\nPackaging Size: ${selectedSize}\n\nPlease let me know availability and delivery options to my location.\n\nThank you.`;
        modalEmailBtn.href = `mailto:${emailAddress}?subject=${encodeURIComponent(emailSubject)}&body=${encodeURIComponent(emailBody)}`;
    };

    const renderSubProductDetails = () => {
        const categoryData = productModalData[activeCategory];
        if (!categoryData) return;

        const subProduct = categoryData.subProducts[activeSubProductIndex];

        // Update main modal image based on sub-product if available, otherwise fallback to category image
        if (subProduct.image) {
            modalProductImg.src = subProduct.image;
        } else {
            modalProductImg.src = categoryData.image;
        }

        // 1. Render Highlights List
        highlightsListContainer.innerHTML = '';
        subProduct.highlights.forEach(highlight => {
            const li = document.createElement('div');
            li.className = 'highlight-bullet';
            li.innerHTML = `<i class="fa-solid fa-circle-check"></i> <span>${highlight}</span>`;
            highlightsListContainer.appendChild(li);
        });

        // 2. Render Specifications Table
        specsTableBody.innerHTML = '';
        for (const [key, val] of Object.entries(subProduct.specs)) {
            const tr = document.createElement('tr');
            tr.innerHTML = `<th>${key}</th><td>${val}</td>`;
            specsTableBody.appendChild(tr);
        }

        // 3. Render Packaging Size Pills
        packagingSizePillsContainer.innerHTML = '';
        subProduct.sizes.forEach((size, index) => {
            const sizeButton = document.createElement('button');
            sizeButton.className = `size-pill ${index === activeSizeIndex ? 'active' : ''}`;
            sizeButton.innerText = size;
            sizeButton.addEventListener('click', () => {
                // Remove active classes
                document.querySelectorAll('#packaging-size-pills .size-pill').forEach(btn => btn.classList.remove('active'));
                // Set active class
                sizeButton.classList.add('active');
                activeSizeIndex = index;
                // Update inquiry buttons with new selected size
                updateModalInquiryButtons();
            });
            packagingSizePillsContainer.appendChild(sizeButton);
        });

        // Update inquiry links
        updateModalInquiryButtons();
    };

    // Global function to trigger modal open from product cards
    window.openProductModal = (categoryKey) => {
        const categoryData = productModalData[categoryKey];
        if (!categoryData) return;

        activeCategory = categoryKey;
        activeSubProductIndex = 0;
        activeSizeIndex = 0;

        // Set static modal details
        modalProductImg.src = categoryData.image;
        modalProductImg.alt = categoryData.title;
        modalCategoryTag.innerText = categoryData.tag;
        modalProductTitle.innerText = categoryData.title;
        modalCategoryDesc.innerText = categoryData.desc;

        // Update Brand Tag Dynamically
        const modalBrandTag = document.querySelector('.modal-image-panel .brand-tag');
        if (modalBrandTag) {
            modalBrandTag.innerText = categoryData.brand || "TIRUMALA BRAND";
        }

        // Render Sub-Product selection pills
        subProductsPillsContainer.innerHTML = '';
        categoryData.subProducts.forEach((sub, index) => {
            const pillButton = document.createElement('button');
            pillButton.className = `size-pill ${index === activeSubProductIndex ? 'active' : ''}`;
            pillButton.innerText = sub.name.replace("Tirumala Floor Cleaner - ", "").replace("Cheetah Floor Cleaner - ", "").replace("Liger Floor Cleaner - ", "").replace("Home Doctor Floor Cleaner - ", "").replace("Tirumala Cleaning Acid - ", "").replace("Horpic Toilet Cleaner - ", "").replace("Tirumala ", "").replace("Coli Fresh ", ""); // Shorter name for buttons
            pillButton.addEventListener('click', () => {
                document.querySelectorAll('#sub-products-pills .size-pill').forEach(btn => btn.classList.remove('active'));
                pillButton.classList.add('active');
                activeSubProductIndex = index;
                activeSizeIndex = 0; // Reset size selection when subproduct changes
                renderSubProductDetails();
            });
            subProductsPillsContainer.appendChild(pillButton);
        });

        // Load the initial sub-product detail view
        renderSubProductDetails();

        // Activate modal overlay
        productModal.classList.add('active');
        document.body.style.overflow = 'hidden'; // prevent scrolling background
    };

    const closeProductModal = () => {
        productModal.classList.remove('active');
        document.body.style.overflow = '';
    };

    if (closeProductModalBtn) {
        closeProductModalBtn.addEventListener('click', closeProductModal);
    }

    if (productModal) {
        productModal.addEventListener('click', (e) => {
            if (e.target === productModal) {
                closeProductModal();
            }
        });
    }

    // Escape Key closing
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && productModal && productModal.classList.contains('active')) {
            closeProductModal();
        }
    });

    // ----------------------------------------------------
    // 7. Scroll-Triggered Animation System (Intersection Observer)
    // ----------------------------------------------------
    const animElements = document.querySelectorAll('.animate-on-scroll');

    const animObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Stop observing once animated
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1, // trigger when 10% of the element is visible
        rootMargin: "0px 0px -40px 0px"
    });

    animElements.forEach(el => {
        animObserver.observe(el);
    });

});
