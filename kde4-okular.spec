%define		_state		stable
%define		orgname		okular
%define		qtver		4.8.1

Summary:	K Desktop Environment - KDE universal document viewer
Summary(pl.UTF-8):	K Desktop Environment - Uniwersalna przeglądarka dokumentów dla KDE
Name:		kde4-okular
Version:	4.8.3
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	4fa7a3edae4197cb93eb80653f184a26
URL:		http://www.kde.org/
BuildRequires:	chmlib-devel
BuildRequires:	djvulibre-devel
BuildRequires:	ebook-tools-devel
BuildRequires:	exiv2-devel >= 0.18.2
BuildRequires:	lcms-devel
BuildRequires:	libgphoto2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libspectre-devel >= 0.2.2
BuildRequires:	poppler-Qt-devel
BuildRequires:	poppler-Qt-devel
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	qimageblitz-devel >= 0.0.6
Obsoletes:	kde4-kdegraphics-okular < 4.6.99
Obsoletes:	kio_msits < 4.6.99
Obsoletes:	okular <= 4.8.0
Suggests:	/usr/bin/lpr
Suggests:	kde4-kdegraphics-mobipocket
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Okular is a universal document browser for KDE.

%description -l pl.UTF-8
Okular to uniwersalna przeglądarka dokumentów dla KDE.

%package devel
Summary:	okular development files
Summary(pl.UTF-8):	Pliki dla programistów okular
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	kde4-kdegraphics-devel < 4.6.99
Obsoletes:	okular-devel < 4.8.0

%description devel
okular development files.

%description devel -l pl.UTF-8
Pliki dla programistów okular.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/okular
%attr(755,root,root) %{_libdir}/libokularcore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libokularcore.so.?
%attr(755,root,root) %{_libdir}/kde4/okular*.so
%attr(755,root,root) %{_libdir}/kde4/kio_msits.so
%{_datadir}/apps/okular
%{_datadir}/config.kcfg/okular.kcfg
%{_datadir}/config.kcfg/gssettings.kcfg
%{_datadir}/kde4/services/okular*.desktop
%{_datadir}/kde4/services/libokular*.desktop
%{_datadir}/kde4/services/msits.protocol
%{_datadir}/kde4/servicetypes/okular*.desktop
%{_desktopdir}/kde4/okular*.desktop
%{_iconsdir}/hicolor/*/apps/okular.png
%{_kdedocdir}/en/okular

%files devel
%defattr(644,root,root,755)
%{_includedir}/okular
%{_libdir}/cmake/Okular
%attr(755,root,root) %{_libdir}/libokularcore.so
