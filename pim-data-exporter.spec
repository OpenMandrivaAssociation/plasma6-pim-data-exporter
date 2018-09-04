%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Allows to save data from KDE PIM applications and restore them in other systems
Name:		pim-data-exporter
Version:	18.08.1
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
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

%description
PIM data exporter allows to save data from KDE PIM applications and restore
them in other systems.

%files -f pimsettingexporter.lang
%{_kde5_applicationsdir}/org.kde.pimsettingexporter.desktop
%{_bindir}/pimsettingexporter
%{_bindir}/pimsettingexporterconsole
%{_datadir}/config.kcfg/pimsettingexporterglobalconfig.kcfg
%{_datadir}/kconf_update/pimsettingexporter*
%{_docdir}/*/*/pimsettingexporter
%{_sysconfdir}/xdg/pimsettingexporter.categories
%{_sysconfdir}/xdg/pimsettingexporter.renamecategories

#----------------------------------------------------------------------------

%define pimsettingexporterprivate_major 5
%define libpimsettingexporterprivate %mklibname pimsettingexporterprivate %{pimsettingexporterprivate_major}

%package -n %{libpimsettingexporterprivate}
Summary:	KDE PIM shared library
Group:		System/Libraries

%description -n %{libpimsettingexporterprivate}
KDE PIM shared library.

%files -n %{libpimsettingexporterprivate}
%{_libdir}/libpimsettingexporterprivate.so.%{pimsettingexporterprivate_major}*

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang pimsettingexporter
