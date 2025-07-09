// Translation System for whatstheirip.tech
// Multi-language dropdown support with enhanced browser language detection

const translations = {
  en: {
    // Navigation
    'nav.pdf': 'PDF',
    'nav.email': 'Email',
    'nav.url': 'URL',
    'nav.viewStats': 'View Stats',
    'nav.images': 'Images',
    
    // Hero Section
    'hero.title1': '🚀 Advanced IP Tracking',
    'hero.title2': 'Made Simple',
    'hero.description': '🌐 Track IP addresses with precision using our advanced suite of tools. Monitor URLs, emails, images, and PDFs with real-time analytics and comprehensive reporting.',
    'hero.viewStats': 'View Your Stats',
    'hero.getStarted': 'Get Started',
    
    // Tracking Code Section
    'tracking.title': 'Enter Your Tracking Code to View Stats',
    'tracking.description': 'Have a tracking code? Enter it below to view your tracking statistics and data.',
    'tracking.label': 'Enter your tracking code:',
    'tracking.placeholder': 'e.g., abc123',
    'tracking.hint': 'Enter your tracking code to view statistics and tracking data',
    'tracking.validFormat': 'Valid tracking code format detected',
    'tracking.statisticsTitle': '📊 Tracking Statistics',
    'tracking.viewStatistics': 'View Statistics',
    'tracking.howToUse': 'How to use: Enter your tracking code above to view detailed statistics including visitor data, locations, devices, and more.',
    
    // Services Section
    'services.title': 'Ways To Track & Logger an IP',
    'services.description': 'Find the geographic location of anyone you\'re interacting with online. This information can be valuable for verification or tracking purposes. Our tools create specialized links that can be shared via social media or messaging to instantly capture IP addresses.',
    'services.urlTracking': 'URL Tracking',
    'services.urlDesc': 'Generate tracked links that log IP data',
    'services.emailTracking': 'Email Tracking',
    'services.emailDesc': 'Invisible images that track email opens',
    'services.notesTracking': 'Notes Tracking',
    'services.notesDesc': 'Create secure notes with tracking',
    
    // URL Tracker Section
    'url.title': 'URL & QR Tracker Generator',
    'url.description': 'Create a tracking link that logs information when someone visits it. You\'ll also get a QR code that points to your tracking link.',
    'url.label': 'Enter the URL you want to track:',
    'url.placeholder': 'https://example.com',
    'url.generateButton': 'Generate Tracking URL/QR',
    'url.trackingUrlTitle': '🔗 Tracking URL',
    'url.trackingCodeTitle': '🔑 Tracking Code',
    'url.shareLink': 'Share this link to track visitor information',
    'url.saveCode': 'Save this code to view tracking results later',
    'url.copyUrl': 'Copy URL',
    'url.copyCode': 'Copy Code',
    'url.viewResults': 'View Results',
    'url.generateHint': 'Generate a tracking link above to populate these fields',
    'url.trackingInfo': 'Your Tracking Information',
    'url.qrCode': 'QR Code',
    'url.qrHint': 'Scan with any QR reader to open the tracking link',
    'url.howItWorks': 'How It Works:',
    'url.step1': 'Enter the URL you want whatstheirip to track',
    'url.step2': 'Drag the progress bar to 100% and click the generate button',
    'url.step3': 'Share the generated tracking link with your target',
    'url.step4': 'Save your tracking code for later reference',
    'url.step5': 'Enter the tracking code on the home page to see captured information'
  },
  
  zh: {
    // Navigation
    'nav.pdf': 'PDF',
    'nav.email': '邮件',
    'nav.url': '网址',
    'nav.viewStats': '查看统计',
    'nav.images': '图片',
    
    // Hero Section
    'hero.title1': '🚀 高级IP追踪',
    'hero.title2': '简单易用',
    'hero.description': '🌐 使用我们的高级工具套件精确追踪IP地址。监控网址、邮件、图片和PDF，提供实时分析和全面报告。',
    'hero.viewStats': '查看您的统计',
    'hero.getStarted': '开始使用',
    
    // Tracking Code Section
    'tracking.title': '输入您的追踪代码查看统计',
    'tracking.description': '已有追踪代码？在下方输入以查看您的追踪统计和数据。',
    'tracking.label': '输入您的追踪代码：',
    'tracking.placeholder': '例如：abc123',
    'tracking.hint': '输入您的追踪代码以查看统计和追踪数据',
    'tracking.validFormat': '检测到有效的追踪代码格式',
    'tracking.statisticsTitle': '📊 追踪统计',
    'tracking.viewStatistics': '查看统计',
    'tracking.howToUse': '使用方法：在上方输入您的追踪代码，查看详细统计包括访客数据、位置、设备等信息。',
    
    // Services Section
    'services.title': '追踪和记录IP的方法',
    'services.description': '查找您在线交互的任何人的地理位置。这些信息对于验证或追踪目的很有价值。我们的工具创建专门的链接，可以通过社交媒体或消息传递分享，即时捕获IP地址。',
    'services.urlTracking': '网址追踪',
    'services.urlDesc': '生成记录IP数据的追踪链接',
    'services.emailTracking': '邮件追踪',
    'services.emailDesc': '追踪邮件打开的隐形图片',
    'services.notesTracking': '笔记追踪',
    'services.notesDesc': '创建带追踪的安全笔记',
    
    // URL Tracker Section
    'url.title': '网址和二维码追踪生成器',
    'url.description': '创建一个追踪链接，当有人访问时记录信息。您还将获得指向追踪链接的二维码。',
    'url.label': '输入您要追踪的网址：',
    'url.placeholder': 'https://example.com',
    'url.generateButton': '生成追踪网址/二维码',
    'url.trackingUrlTitle': '🔗 追踪网址',
    'url.trackingCodeTitle': '🔑 追踪代码',
    'url.shareLink': '分享此链接以追踪访客信息',
    'url.saveCode': '保存此代码以便稍后查看追踪结果',
    'url.copyUrl': '复制网址',
    'url.copyCode': '复制代码',
    'url.viewResults': '查看结果',
    'url.generateHint': '在上方生成追踪链接以填充这些字段',
    'url.trackingInfo': '您的追踪信息',
    'url.qrCode': '二维码',
    'url.qrHint': '使用任何二维码阅读器扫描以打开追踪链接',
    'url.howItWorks': '工作原理：',
    'url.step1': '输入您希望whatstheirip追踪的网址',
    'url.step2': '将进度条拖到100%并点击生成按钮',
    'url.step3': '与您的目标分享生成的追踪链接',
    'url.step4': '保存您的追踪代码以供稍后参考',
    'url.step5': '在首页输入追踪代码查看捕获的信息'
  },
  
  fr: {
    // Navigation
    'nav.pdf': 'PDF',
    'nav.email': 'Email',
    'nav.url': 'URL',
    'nav.viewStats': 'Voir Stats',
    'nav.images': 'Images',
    
    // Hero Section
    'hero.title1': '🚀 Suivi IP Avancé',
    'hero.title2': 'Rendu Simple',
    'hero.description': '🌐 Suivez les adresses IP avec précision en utilisant notre suite d\'outils avancés. Surveillez les URLs, emails, images et PDFs avec des analyses en temps réel et des rapports complets.',
    'hero.viewStats': 'Voir Vos Stats',
    'hero.getStarted': 'Commencer',
    
    // Tracking Code Section
    'tracking.title': 'Entrez Votre Code de Suivi pour Voir les Stats',
    'tracking.description': 'Vous avez un code de suivi ? Entrez-le ci-dessous pour voir vos statistiques et données de suivi.',
    'tracking.label': 'Entrez votre code de suivi:',
    'tracking.placeholder': 'ex: abc123',
    'tracking.hint': 'Entrez votre code de suivi pour voir les statistiques et données de suivi',
    'tracking.validFormat': 'Format de code de suivi valide détecté',
    'tracking.statisticsTitle': '📊 Statistiques de Suivi',
    'tracking.viewStatistics': 'Voir Statistiques',
    'tracking.howToUse': 'Comment utiliser: Entrez votre code de suivi ci-dessus pour voir les statistiques détaillées incluant les données des visiteurs, emplacements, appareils et plus.',
    
    // Services Section
    'services.title': 'Moyens de Suivre et Enregistrer une IP',
    'services.description': 'Trouvez l\'emplacement géographique de toute personne avec qui vous interagissez en ligne. Ces informations peuvent être précieuses à des fins de vérification ou de suivi.',
    'services.urlTracking': 'Suivi URL',
    'services.urlDesc': 'Générer des liens suivis qui enregistrent les données IP',
    'services.emailTracking': 'Suivi Email',
    'services.emailDesc': 'Images invisibles qui suivent les ouvertures d\'emails',
    'services.notesTracking': 'Suivi de Notes',
    'services.notesDesc': 'Créer des notes sécurisées avec suivi',
    
    // URL Tracker Section
    'url.title': 'Générateur de Suivi URL et QR',
    'url.description': 'Créez un lien de suivi qui enregistre les informations lorsque quelqu\'un le visite. Vous obtiendrez également un code QR pointant vers votre lien de suivi.',
    'url.label': 'Entrez l\'URL que vous voulez suivre:',
    'url.placeholder': 'https://example.com',
    'url.generateButton': 'Générer URL/QR de Suivi',
    'url.trackingUrlTitle': '🔗 URL de Suivi',
    'url.trackingCodeTitle': '🔑 Code de Suivi',
    'url.shareLink': 'Partagez ce lien pour suivre les informations des visiteurs',
    'url.saveCode': 'Sauvegardez ce code pour voir les résultats de suivi plus tard',
    'url.copyUrl': 'Copier URL',
    'url.copyCode': 'Copier Code',
    'url.viewResults': 'Voir Résultats',
    'url.generateHint': 'Générez un lien de suivi ci-dessus pour remplir ces champs',
    'url.trackingInfo': 'Vos Informations de Suivi',
    'url.qrCode': 'Code QR',
    'url.qrHint': 'Scannez avec n\'importe quel lecteur QR pour ouvrir le lien de suivi',
    'url.howItWorks': 'Comment ça marche:',
    'url.step1': 'Entrez l\'URL que vous voulez que whatstheirip suive',
    'url.step2': 'Faites glisser la barre de progression à 100% et cliquez sur générer',
    'url.step3': 'Partagez le lien de suivi généré avec votre cible',
    'url.step4': 'Sauvegardez votre code de suivi pour référence ultérieure',
    'url.step5': 'Entrez le code de suivi sur la page d\'accueil pour voir les informations capturées'
  },
  
  de: {
    // Navigation
    'nav.pdf': 'PDF',
    'nav.email': 'E-Mail',
    'nav.url': 'URL',
    'nav.viewStats': 'Stats Anzeigen',
    'nav.images': 'Bilder',
    
    // Hero Section
    'hero.title1': '🚀 Erweiterte IP-Verfolgung',
    'hero.title2': 'Einfach Gemacht',
    'hero.description': '🌐 Verfolgen Sie IP-Adressen präzise mit unserer erweiterten Tool-Suite. Überwachen Sie URLs, E-Mails, Bilder und PDFs mit Echtzeitanalysen und umfassenden Berichten.',
    'hero.viewStats': 'Ihre Stats Anzeigen',
    'hero.getStarted': 'Loslegen',
    
    // Tracking Code Section
    'tracking.title': 'Geben Sie Ihren Tracking-Code ein, um Stats zu sehen',
    'tracking.description': 'Haben Sie einen Tracking-Code? Geben Sie ihn unten ein, um Ihre Tracking-Statistiken und -Daten anzuzeigen.',
    'tracking.label': 'Geben Sie Ihren Tracking-Code ein:',
    'tracking.placeholder': 'z.B.: abc123',
    'tracking.hint': 'Geben Sie Ihren Tracking-Code ein, um Statistiken und Tracking-Daten anzuzeigen',
    'tracking.validFormat': 'Gültiges Tracking-Code-Format erkannt',
    'tracking.statisticsTitle': '📊 Tracking-Statistiken',
    'tracking.viewStatistics': 'Statistiken Anzeigen',
    'tracking.howToUse': 'Verwendung: Geben Sie Ihren Tracking-Code oben ein, um detaillierte Statistiken einschließlich Besucherdaten, Standorte, Geräte und mehr anzuzeigen.',
    
    // Services Section
    'services.title': 'Wege zum Verfolgen und Protokollieren einer IP',
    'services.description': 'Finden Sie den geografischen Standort von jedem, mit dem Sie online interagieren. Diese Informationen können für Verifizierungs- oder Tracking-Zwecke wertvoll sein.',
    'services.urlTracking': 'URL-Verfolgung',
    'services.urlDesc': 'Generieren Sie verfolgte Links, die IP-Daten protokollieren',
    'services.emailTracking': 'E-Mail-Verfolgung',
    'services.emailDesc': 'Unsichtbare Bilder, die E-Mail-Öffnungen verfolgen',
    'services.notesTracking': 'Notizen-Verfolgung',
    'services.notesDesc': 'Erstellen Sie sichere Notizen mit Verfolgung',
    
    // URL Tracker Section
    'url.title': 'URL & QR Tracking-Generator',
    'url.description': 'Erstellen Sie einen Tracking-Link, der Informationen protokolliert, wenn jemand ihn besucht. Sie erhalten auch einen QR-Code, der auf Ihren Tracking-Link zeigt.',
    'url.label': 'Geben Sie die URL ein, die Sie verfolgen möchten:',
    'url.placeholder': 'https://example.com',
    'url.generateButton': 'Tracking-URL/QR Generieren',
    'url.trackingUrlTitle': '🔗 Tracking-URL',
    'url.trackingCodeTitle': '🔑 Tracking-Code',
    'url.shareLink': 'Teilen Sie diesen Link, um Besucherinformationen zu verfolgen',
    'url.saveCode': 'Speichern Sie diesen Code, um Tracking-Ergebnisse später anzuzeigen',
    'url.copyUrl': 'URL Kopieren',
    'url.copyCode': 'Code Kopieren',
    'url.viewResults': 'Ergebnisse Anzeigen',
    'url.generateHint': 'Generieren Sie einen Tracking-Link oben, um diese Felder zu füllen',
    'url.trackingInfo': 'Ihre Tracking-Informationen',
    'url.qrCode': 'QR-Code',
    'url.qrHint': 'Mit jedem QR-Reader scannen, um den Tracking-Link zu öffnen',
    'url.howItWorks': 'Wie es funktioniert:',
    'url.step1': 'Geben Sie die URL ein, die whatstheirip verfolgen soll',
    'url.step2': 'Ziehen Sie die Fortschrittsleiste auf 100% und klicken Sie auf Generieren',
    'url.step3': 'Teilen Sie den generierten Tracking-Link mit Ihrem Ziel',
    'url.step4': 'Speichern Sie Ihren Tracking-Code zur späteren Referenz',
    'url.step5': 'Geben Sie den Tracking-Code auf der Startseite ein, um erfasste Informationen zu sehen'
  },
  
  es: {
    // Navigation
    'nav.pdf': 'PDF',
    'nav.email': 'Correo',
    'nav.url': 'URL',
    'nav.viewStats': 'Ver Estadísticas',
    'nav.images': 'Imágenes',
    
    // Hero Section
    'hero.title1': '🚀 Rastreo IP Avanzado',
    'hero.title2': 'Hecho Simple',
    'hero.description': '🌐 Rastrea direcciones IP con precisión usando nuestro conjunto avanzado de herramientas. Monitorea URLs, correos, imágenes y PDFs con análisis en tiempo real y reportes comprehensivos.',
    'hero.viewStats': 'Ver Tus Estadísticas',
    'hero.getStarted': 'Comenzar',
    
    // Tracking Code Section
    'tracking.title': 'Ingresa Tu Código de Rastreo para Ver Estadísticas',
    'tracking.description': '¿Tienes un código de rastreo? Ingrésalo abajo para ver tus estadísticas y datos de rastreo.',
    'tracking.label': 'Ingresa tu código de rastreo:',
    'tracking.placeholder': 'ej: abc123',
    'tracking.hint': 'Ingresa tu código de rastreo para ver estadísticas y datos de rastreo',
    'tracking.validFormat': 'Formato de código de rastreo válido detectado',
    'tracking.statisticsTitle': '📊 Estadísticas de Rastreo',
    'tracking.viewStatistics': 'Ver Estadísticas',
    'tracking.howToUse': 'Cómo usar: Ingresa tu código de rastreo arriba para ver estadísticas detalladas incluyendo datos de visitantes, ubicaciones, dispositivos y más.',
    
    // Services Section
    'services.title': 'Maneras de Rastrear y Registrar una IP',
    'services.description': 'Encuentra la ubicación geográfica de cualquier persona con la que interactúas en línea. Esta información puede ser valiosa para propósitos de verificación o rastreo.',
    'services.urlTracking': 'Rastreo de URL',
    'services.urlDesc': 'Genera enlaces rastreados que registran datos IP',
    'services.emailTracking': 'Rastreo de Correo',
    'services.emailDesc': 'Imágenes invisibles que rastrean aperturas de correos',
    'services.notesTracking': 'Rastreo de Notas',
    'services.notesDesc': 'Crea notas seguras con rastreo',
    
    // URL Tracker Section
    'url.title': 'Generador de Rastreo URL y QR',
    'url.description': 'Crea un enlace de rastreo que registra información cuando alguien lo visita. También obtendrás un código QR que apunta a tu enlace de rastreo.',
    'url.label': 'Ingresa la URL que quieres rastrear:',
    'url.placeholder': 'https://example.com',
    'url.generateButton': 'Generar URL/QR de Rastreo',
    'url.trackingUrlTitle': '🔗 URL de Rastreo',
    'url.trackingCodeTitle': '🔑 Código de Rastreo',
    'url.shareLink': 'Comparte este enlace para rastrear información de visitantes',
    'url.saveCode': 'Guarda este código para ver resultados de rastreo más tarde',
    'url.copyUrl': 'Copiar URL',
    'url.copyCode': 'Copiar Código',
    'url.viewResults': 'Ver Resultados',
    'url.generateHint': 'Genera un enlace de rastreo arriba para llenar estos campos',
    'url.trackingInfo': 'Tu Información de Rastreo',
    'url.qrCode': 'Código QR',
    'url.qrHint': 'Escanea con cualquier lector QR para abrir el enlace de rastreo',
    'url.howItWorks': 'Cómo funciona:',
    'url.step1': 'Ingresa la URL que quieres que whatstheirip rastree',
    'url.step2': 'Arrastra la barra de progreso al 100% y haz clic en generar',
    'url.step3': 'Comparte el enlace de rastreo generado con tu objetivo',
    'url.step4': 'Guarda tu código de rastreo para referencia posterior',
    'url.step5': 'Ingresa el código de rastreo en la página principal para ver información capturada'
  },
  
  ko: {
    // Navigation
    'nav.pdf': 'PDF',
    'nav.email': '이메일',
    'nav.url': 'URL',
    'nav.viewStats': '통계 보기',
    'nav.images': '이미지',
    
    // Hero Section
    'hero.title1': '🚀 고급 IP 추적',
    'hero.title2': '간단하게',
    'hero.description': '🌐 고급 도구 모음을 사용하여 IP 주소를 정확하게 추적하세요. URL, 이메일, 이미지 및 PDF를 실시간 분석과 포괄적인 보고서로 모니터링하세요.',
    'hero.viewStats': '통계 보기',
    'hero.getStarted': '시작하기',
    
    // Tracking Code Section
    'tracking.title': '추적 코드를 입력하여 통계 보기',
    'tracking.description': '추적 코드가 있으신가요? 아래에 입력하여 추적 통계와 데이터를 확인하세요.',
    'tracking.label': '추적 코드를 입력하세요:',
    'tracking.placeholder': '예: abc123',
    'tracking.hint': '추적 코드를 입력하여 통계와 추적 데이터를 확인하세요',
    'tracking.validFormat': '유효한 추적 코드 형식이 감지됨',
    'tracking.statisticsTitle': '📊 추적 통계',
    'tracking.viewStatistics': '통계 보기',
    'tracking.howToUse': '사용법: 위에 추적 코드를 입력하여 방문자 데이터, 위치, 기기 등을 포함한 자세한 통계를 확인하세요.',
    
    // Services Section
    'services.title': 'IP 추적 및 로깅 방법',
    'services.description': '온라인에서 상호작용하는 모든 사람의 지리적 위치를 찾으세요. 이 정보는 검증이나 추적 목적으로 유용할 수 있습니다.',
    'services.urlTracking': 'URL 추적',
    'services.urlDesc': 'IP 데이터를 기록하는 추적 링크 생성',
    'services.emailTracking': '이메일 추적',
    'services.emailDesc': '이메일 열림을 추적하는 보이지 않는 이미지',
    'services.notesTracking': '노트 추적',
    'services.notesDesc': '추적 기능이 있는 보안 노트 생성',
    
    // URL Tracker Section
    'url.title': 'URL 및 QR 추적 생성기',
    'url.description': '누군가 방문할 때 정보를 기록하는 추적 링크를 만드세요. 추적 링크를 가리키는 QR 코드도 얻을 수 있습니다.',
    'url.label': '추적하려는 URL을 입력하세요:',
    'url.placeholder': 'https://example.com',
    'url.generateButton': '추적 URL/QR 생성',
    'url.trackingUrlTitle': '🔗 추적 URL',
    'url.trackingCodeTitle': '🔑 추적 코드',
    'url.shareLink': '이 링크를 공유하여 방문자 정보 추적',
    'url.saveCode': '나중에 추적 결과를 보기 위해 이 코드를 저장하세요',
    'url.copyUrl': 'URL 복사',
    'url.copyCode': '코드 복사',
    'url.viewResults': '결과 보기',
    'url.generateHint': '위에서 추적 링크를 생성하여 이 필드들을 채우세요',
    'url.trackingInfo': '추적 정보',
    'url.qrCode': 'QR 코드',
    'url.qrHint': 'QR 리더로 스캔하여 추적 링크 열기',
    'url.howItWorks': '작동 방식:',
    'url.step1': 'whatstheirip이 추적할 URL을 입력하세요',
    'url.step2': '진행 바를 100%로 드래그하고 생성 버튼을 클릭하세요',
    'url.step3': '생성된 추적 링크를 대상과 공유하세요',
    'url.step4': '나중에 참조할 수 있도록 추적 코드를 저장하세요',
    'url.step5': '홈페이지에 추적 코드를 입력하여 캡처된 정보를 확인하세요'
  }
};

// Language configuration with flags and names
const languageConfig = {
  en: { name: 'English', flag: '🇺🇸', nativeName: 'English' },
  zh: { name: 'Chinese', flag: '🇨🇳', nativeName: '中文' },
  fr: { name: 'French', flag: '🇫🇷', nativeName: 'Français' },
  de: { name: 'German', flag: '🇩🇪', nativeName: 'Deutsch' },
  es: { name: 'Spanish', flag: '🇪🇸', nativeName: 'Español' },
  ko: { name: 'Korean', flag: '🇰🇷', nativeName: '한국어' }
};

// Current language
let currentLanguage = 'en';

// Translation functions
function translate(key) {
  return translations[currentLanguage]?.[key] || translations['en']?.[key] || key;
}

function translatePage() {
  // Find all elements with data-translate attribute
  const elements = document.querySelectorAll('[data-translate]');
  
  elements.forEach(element => {
    const key = element.getAttribute('data-translate');
    const translatedText = translate(key);
    
    // Handle different element types
    if (element.tagName === 'INPUT') {
      if (element.type === 'text' || element.type === 'search') {
        element.placeholder = translatedText;
      } else {
        element.value = translatedText;
      }
    } else if (element.tagName === 'IMG') {
      element.alt = translatedText;
    } else {
      element.textContent = translatedText;
    }
  });
  
  // Update dynamic content
  updateDynamicContent();
}

function updateDynamicContent() {
  // Update range slider text
  const rangeValue = document.getElementById('rangeValue');
  const rangeValue2 = document.getElementById('rangeValue2');
  
  const dragText = {
    en: 'Drag Progress Bar to the End',
    zh: '将进度条拖到末端',
    fr: 'Faites glisser la barre de progression jusqu\'à la fin',
    de: 'Ziehen Sie die Fortschrittsleiste bis zum Ende',
    es: 'Arrastra la barra de progreso hasta el final',
    ko: '진행 바를 끝까지 드래그하세요'
  };
  
  const readyText = {
    en: 'You\'re Good to Go',
    zh: '准备就绪',
    fr: 'Vous êtes prêt',
    de: 'Sie sind bereit',
    es: 'Estás listo',
    ko: '준비 완료'
  };
  
  if (rangeValue) {
    if (rangeValue.textContent.includes('Good to Go') || rangeValue.textContent.includes('준비') || rangeValue.textContent.includes('prêt') || rangeValue.textContent.includes('bereit') || rangeValue.textContent.includes('listo') || rangeValue.textContent.includes('준비')) {
      rangeValue.textContent = readyText[currentLanguage] || readyText.en;
    } else {
      rangeValue.textContent = dragText[currentLanguage] || dragText.en;
    }
  }
  
  if (rangeValue2) {
    if (rangeValue2.textContent.includes('Good to Go') || rangeValue2.textContent.includes('준비') || rangeValue2.textContent.includes('prêt') || rangeValue2.textContent.includes('bereit') || rangeValue2.textContent.includes('listo') || rangeValue2.textContent.includes('준비')) {
      rangeValue2.textContent = readyText[currentLanguage] || readyText.en;
    } else {
      rangeValue2.textContent = dragText[currentLanguage] || dragText.en;
    }
  }
}

function switchLanguage(lang) {
  console.log('Switching to language:', lang);
  
  if (languageConfig[lang]) {
    currentLanguage = lang;
    localStorage.setItem('preferredLanguage', currentLanguage);
    translatePage();
    updateLanguageButton();
    closeLanguageDropdown();
  }
}

function updateLanguageButton() {
  const langButton = document.getElementById('languageToggle');
  if (langButton) {
    const config = languageConfig[currentLanguage];
    langButton.innerHTML = `
      <span class="flag-icon">${config.flag}</span>
      <span class="lang-name">${config.nativeName}</span>
      <i class="fas fa-chevron-down ml-1"></i>
    `;
  }
}

function toggleLanguageDropdown() {
  const dropdown = document.getElementById('languageDropdown');
  if (dropdown) {
    const isVisible = dropdown.classList.contains('show');
    if (isVisible) {
      dropdown.classList.remove('show');
      setTimeout(() => {
        dropdown.style.display = 'none';
      }, 300);
    } else {
      dropdown.style.display = 'block';
      setTimeout(() => {
        dropdown.classList.add('show');
      }, 10);
    }
  }
}

function closeLanguageDropdown() {
  const dropdown = document.getElementById('languageDropdown');
  if (dropdown) {
    dropdown.classList.remove('show');
    setTimeout(() => {
      dropdown.style.display = 'none';
    }, 300);
  }
}

function createLanguageDropdown() {
  const dropdown = document.createElement('div');
  dropdown.id = 'languageDropdown';
  dropdown.className = 'language-dropdown';
  dropdown.style.display = 'none';
  
  Object.keys(languageConfig).forEach(langCode => {
    const config = languageConfig[langCode];
    const option = document.createElement('div');
    option.className = `language-option ${currentLanguage === langCode ? 'active' : ''}`;
    option.onclick = () => switchLanguage(langCode);
    option.innerHTML = `
      <span class="flag-icon">${config.flag}</span>
      <span class="lang-name">${config.nativeName}</span>
      ${currentLanguage === langCode ? '<i class="fas fa-check ml-auto"></i>' : ''}
    `;
    dropdown.appendChild(option);
  });
  
  return dropdown;
}

// Enhanced browser language detection
function detectBrowserLanguage() {
  // Get all possible language preferences from browser
  const browserLanguages = [
    navigator.language,
    navigator.userLanguage,
    navigator.browserLanguage,
    navigator.systemLanguage,
    ...(navigator.languages || [])
  ].filter(Boolean); // Remove undefined values

  console.log('Browser languages detected:', browserLanguages);

  // Language mapping for better detection
  const languageMapping = {
    // English variants
    'en': 'en', 'en-US': 'en', 'en-GB': 'en', 'en-CA': 'en', 'en-AU': 'en',
    
    // Chinese variants
    'zh': 'zh', 'zh-CN': 'zh', 'zh-Hans': 'zh', 'zh-SG': 'zh',
    'zh-TW': 'zh', 'zh-Hant': 'zh', 'zh-HK': 'zh', 'zh-MO': 'zh',
    
    // French variants
    'fr': 'fr', 'fr-FR': 'fr', 'fr-CA': 'fr', 'fr-BE': 'fr', 'fr-CH': 'fr',
    
    // German variants
    'de': 'de', 'de-DE': 'de', 'de-AT': 'de', 'de-CH': 'de',
    
    // Spanish variants
    'es': 'es', 'es-ES': 'es', 'es-MX': 'es', 'es-AR': 'es', 'es-CO': 'es',
    'es-PE': 'es', 'es-VE': 'es', 'es-CL': 'es', 'es-UY': 'es',
    
    // Korean variants
    'ko': 'ko', 'ko-KR': 'ko'
  };

  // Try to find exact match first
  for (const browserLang of browserLanguages) {
    if (languageMapping[browserLang]) {
      const detectedLang = languageMapping[browserLang];
      if (languageConfig[detectedLang]) {
        console.log(`Exact language match found: ${browserLang} -> ${detectedLang}`);
        return detectedLang;
      }
    }
  }

  // Try to find partial match (language prefix)
  for (const browserLang of browserLanguages) {
    const langPrefix = browserLang.split('-')[0].toLowerCase();
    if (languageConfig[langPrefix]) {
      console.log(`Partial language match found: ${browserLang} -> ${langPrefix}`);
      return langPrefix;
    }
  }

  // Try alternative matching for common cases
  for (const browserLang of browserLanguages) {
    const lowerLang = browserLang.toLowerCase();
    
    // Special cases for Chinese
    if (lowerLang.includes('chinese') || lowerLang.includes('中文')) {
      console.log(`Chinese language detected: ${browserLang} -> zh`);
      return 'zh';
    }
    
    // Special cases for other languages
    if (lowerLang.includes('korean') || lowerLang.includes('한국')) {
      console.log(`Korean language detected: ${browserLang} -> ko`);
      return 'ko';
    }
    
    if (lowerLang.includes('spanish') || lowerLang.includes('español')) {
      console.log(`Spanish language detected: ${browserLang} -> es`);
      return 'es';
    }
    
    if (lowerLang.includes('french') || lowerLang.includes('français')) {
      console.log(`French language detected: ${browserLang} -> fr`);
      return 'fr';
    }
    
    if (lowerLang.includes('german') || lowerLang.includes('deutsch')) {
      console.log(`German language detected: ${browserLang} -> de`);
      return 'de';
    }
  }

  // Default to English if no match found
  console.log('No language match found, defaulting to English');
  return 'en';
}

// Enhanced initialization with better language detection
function initializeTranslations() {
  console.log('Initializing translations with enhanced browser detection...');
  
  // Check for saved language preference first (user's explicit choice takes priority)
  const savedLanguage = localStorage.getItem('preferredLanguage');
  if (savedLanguage && languageConfig[savedLanguage]) {
    currentLanguage = savedLanguage;
    console.log(`Using saved language preference: ${currentLanguage}`);
  } else {
    // Use enhanced browser language detection
    currentLanguage = detectBrowserLanguage();
    console.log(`Auto-detected language: ${currentLanguage}`);
    
    // Save the detected language as user preference
    localStorage.setItem('preferredLanguage', currentLanguage);
  }
  
  // Show language detection result to user (optional)
  if (currentLanguage !== 'en') {
    console.log(`🌐 Language auto-detected: ${languageConfig[currentLanguage].nativeName}`);
    
    // Optional: Show a brief notification to user about language detection
    showLanguageDetectionNotification();
  }
  
  // Create and insert language dropdown
  const langToggle = document.getElementById('languageToggle');
  if (langToggle && !document.getElementById('languageDropdown')) {
    const dropdown = createLanguageDropdown();
    langToggle.parentElement.appendChild(dropdown);
    langToggle.parentElement.style.position = 'relative';
  }
  
  // Translate page on load
  translatePage();
  updateLanguageButton();
  
  // Close dropdown when clicking outside
  document.addEventListener('click', (event) => {
    const langToggle = document.getElementById('languageToggle');
    const langDropdown = document.getElementById('languageDropdown');
    
    if (langToggle && langDropdown && 
        !langToggle.contains(event.target) && 
        !langDropdown.contains(event.target)) {
      closeLanguageDropdown();
    }
  });
}

// Optional: Show a brief notification about language detection
function showLanguageDetectionNotification() {
  // Only show if language was auto-detected (not previously saved)
  const wasAutoDetected = !localStorage.getItem('languageDetectionShown');
  
  if (wasAutoDetected && currentLanguage !== 'en') {
    setTimeout(() => {
      const notification = document.createElement('div');
      notification.style.cssText = `
        position: fixed;
        top: 80px;
        right: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 12px 20px;
        border-radius: 25px;
        font-size: 14px;
        font-weight: 500;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
        z-index: 10000;
        opacity: 0;
        transform: translateX(100%);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      `;
      
      const flag = languageConfig[currentLanguage].flag;
      const name = languageConfig[currentLanguage].nativeName;
      notification.innerHTML = `${flag} Language detected: ${name}`;
      
      document.body.appendChild(notification);
      
      // Animate in
      setTimeout(() => {
        notification.style.opacity = '1';
        notification.style.transform = 'translateX(0)';
      }, 100);
      
      // Animate out after 3 seconds
      setTimeout(() => {
        notification.style.opacity = '0';
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
          if (notification.parentNode) {
            notification.parentNode.removeChild(notification);
          }
        }, 300);
      }, 3000);
      
      // Mark as shown
      localStorage.setItem('languageDetectionShown', 'true');
    }, 1000); // Delay to let page load first
  }
}

// Add a manual language reset function for testing
function resetLanguageDetection() {
  localStorage.removeItem('preferredLanguage');
  localStorage.removeItem('languageDetectionShown');
  location.reload();
}

// Export the reset function for debugging
window.resetLanguageDetection = resetLanguageDetection;

// Initialize translations on DOM ready
document.addEventListener('DOMContentLoaded', initializeTranslations);

// Make functions available globally
window.toggleLanguageDropdown = toggleLanguageDropdown;
window.switchLanguage = switchLanguage;
window.translate = translate;
window.translatePage = translatePage;

// Handle language switch function for button onclick
window.handleLanguageSwitch = function() {
  toggleLanguageDropdown();
};
