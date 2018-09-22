Summary:	A vi-like pdf reader
Summary(hu.UTF-8):	Egy vi-szerű pdf olvasó
Summary(pl.UTF-8):	Czytnik pdf podobny do vi
Name:		zathura
Version:	0.4.1
Release:	1
License:	BSD-like
Group:		Applications
Source0:	http://pwmt.org/projects/zathura/download/%{name}-%{version}.tar.xz
# Source0-md5:	50495884064e3c127304a5b6390c836c
Source1:	config.txt
URL:		http://pwmt.org/projects/zathura
BuildRequires:	cairo-devel
BuildRequires:	girara-devel >= 0.2.9
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	intltool
BuildRequires:	libmagic-devel
BuildRequires:	meson >= 0.45
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	python-docutils
BuildRequires:	rpmbuild(macros) >= 1.727
BuildRequires:	sqlite3-devel >= 3.5.9
Requires(post,postun):	gtk-update-icon-cache
Requires:	girara >= 0.2.9
Requires:	glib2 >= 1:2.50.0
Requires:	gtk+3 >= 3.22
Requires:	hicolor-icon-theme
Requires:	sqlite3 >= 3.5.9
Suggests:	zathura-pdf-poppler
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zathura is a highly customizable and functional PDF viewer based on
the poppler rendering library and the gtk+ toolkit. The idea behind
zathura is an application that provides a minimalistic and space
saving interface as well as an easy usage that mainly focuses on
keyboard interaction.

%description -l hu.UTF-8
zathura egy magas szinten konfigurálható és funkcionális PDF olvasó a
poppler és gtk+ könyvtárako alapulva. A zathura célja, hogy egy olyan
alkalmazás legyen, amely minimalista és terület-takarékos felületet
biztosítson, amennyire lehet, és könnyen lehessen használni, főleg
billentyűzet segítségével.

%description -l pl.UTF-8
zathura jest wysoko konfigurowalnym i funkcjonalnym wyświetlaczem PDF
opartym na bibliotece renderującej poppler i zestawie narzędziowym
gtk+. zathura jest aplikacją, która udostępnia minimalistyczny i nie
zajmujący dużo miejsca interfejs, który jednocześnie jest prosty w
użyciu. Interfejs skupia się głównie na interakcji klawiaturowej.

%package devel
Summary:	Header files for zathura
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for zathura.

%prep
%setup -q
cp %{SOURCE1} config.txt

%build
%meson build
%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/%{name}

%meson_install -C build

%{__mv} $RPM_BUILD_ROOT%{_localedir}/id_ID $RPM_BUILD_ROOT%{_localedir}/id
%{__mv} $RPM_BUILD_ROOT%{_localedir}/no $RPM_BUILD_ROOT%{_localedir}/nb
%{__mv} $RPM_BUILD_ROOT%{_localedir}/ta_IN $RPM_BUILD_ROOT%{_localedir}/ta
%{__mv} $RPM_BUILD_ROOT%{_localedir}/uk_UA $RPM_BUILD_ROOT%{_localedir}/uk

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc LICENSE README config.txt
%attr(755,root,root) %{_bindir}/zathura
%{_desktopdir}/org.pwmt.zathura.desktop
%{_datadir}/metainfo/org.pwmt.zathura.appdata.xml
%{_datadir}/dbus-1/interfaces/org.pwmt.zathura.xml
%{_iconsdir}/hicolor/*/apps/org.pwmt.zathura.png
%{_mandir}/man1/zathura.1*
%{_mandir}/man5/zathurarc.5*
%dir %{_libdir}/zathura

%files devel
%defattr(644,root,root,755)
%{_includedir}/zathura
%{_pkgconfigdir}/zathura.pc
