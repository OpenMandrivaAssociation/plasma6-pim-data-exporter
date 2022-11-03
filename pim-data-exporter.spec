%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Allows to save data from KDE PIM applications and restore them in other systems
Name:		pim-data-exporter
Version:	22.08.3
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		pim-data-exporter-More-menu.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5IdentityManagement)
BuildRequires:	cmake(KF5Libkdepim)
BuildRequires:	cmake(KF5MailCommon)
BuildRequires:	cmake(KF5MailTransport)
BuildRequires:	cmake(KF5Mime)
BuildRequires:	cmake(KF5PimCommonAkonadi)
BuildRequires:	cmake(KF5PimTextEdit)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5AkonadiNotes)
BuildRequires:	cmake(KUserFeedback)
BuildRequires:	cmake(QGpgme)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
Provides:	pimsettingexporter = %{EVRD}
Conflicts:	pimsettingexporter < 3:17.04.0
Obsoletes:	pimsettingexporter < 3:17.04.0
%define pimsettingexporterprivate_major 5
%define libpimsettingexporterprivate %mklibname pimsettingexporterprivate %{pimsettingexporterprivate_major}
Obsoletes: %{libpimsettingexporterprivate} < %{EVRD}


%description
PIM data exporter allows to save data from KDE PIM applications and restore
them in other systems.


#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang pimdataexporter --with-html --all-name

%files -f pimdataexporter.lang
%{_datadir}/metainfo/org.kde.pimdataexporter.appdata.xml
%{_datadir}/qlogging-categories5/pimdataexporter.categories
%{_datadir}/qlogging-categories5/pimdataexporter.renamecategories
%{_bindir}/pimdataexporter
%{_bindir}/pimdataexporterconsole
%{_libdir}/libpimdataexporterprivate.so.*
%{_datadir}/applications/org.kde.pimdataexporter.desktop
%{_datadir}/config.kcfg/pimdataexporterglobalconfig.kcfg

