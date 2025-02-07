#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Allows to save data from KDE PIM applications and restore them in other systems
Name:		plasma6-pim-data-exporter
Version:	24.12.2
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/pim-data-exporter/-/archive/%{gitbranch}/pim-data-exporter-%{gitbranchd}.tar.bz2#/pim-data-exporter-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/pim-data-exporter-%{version}.tar.xz
%endif
Patch0:		pim-data-exporter-More-menu.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	cmake(KPim6IdentityManagementCore)
BuildRequires:	cmake(KPim6Libkdepim)
BuildRequires:	cmake(KPim6MailCommon)
BuildRequires:	cmake(KPim6MailTransport)
BuildRequires:	cmake(KPim6Mime)
BuildRequires:	cmake(KPim6PimCommonAkonadi)
BuildRequires:	cmake(KPim6TextEdit)
BuildRequires:	cmake(KF6CalendarCore)
BuildRequires:	cmake(KPim6AkonadiNotes)
BuildRequires:	cmake(KF6UserFeedback)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	cmake(KF6TextTemplate)
BuildRequires:	cmake(QGpgme)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Xml)
BuildRequires:	%mklibname -d KF6UserFeedbackWidgets
%define pimsettingexporterprivate_major 6
%define libpimsettingexporterprivate %mklibname pimsettingexporterprivate %{pimsettingexporterprivate_major}
Obsoletes: %{libpimsettingexporterprivate} < %{EVRD}


%description
PIM data exporter allows to save data from KDE PIM applications and restore
them in other systems.


#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n pim-data-exporter-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang pimdataexporter --with-html --all-name

%files -f pimdataexporter.lang
%{_datadir}/metainfo/org.kde.pimdataexporter.appdata.xml
%{_datadir}/qlogging-categories6/pimdataexporter.categories
%{_datadir}/qlogging-categories6/pimdataexporter.renamecategories
%{_bindir}/pimdataexporter
%{_bindir}/pimdataexporterconsole
%{_libdir}/libpimdataexporterprivate.so.*
%{_datadir}/applications/org.kde.pimdataexporter.desktop
%{_datadir}/config.kcfg/pimdataexporterglobalconfig.kcfg

