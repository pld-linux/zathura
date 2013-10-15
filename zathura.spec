Summary:	A vi-like pdf reader
Summary(hu.UTF-8):	Egy vi-szerű pdf olvasó
Summary(pl.UTF-8):	Czytnik pdf podobny do vi
Name:		zathura
Version:	0.2.4
Release:	2
License:	BSD-like
Group:		Applications
Source0:	https://pwmt.org/projects/zathura/download/%{name}-%{version}.tar.gz
# Source0-md5:	935c6e15f5b7688bf4024ec7fe45f064
Source1:	config.txt
URL:		http://pwmt.org/projects/zathura
BuildRequires:	girara-devel >= 0.1.6
BuildRequires:	gtk+2-devel >= 2:2.18.6
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel >= 3.5.9
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
%{__mv} po/id_ID.po po/id.po

%build
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} \
	VERBOSE=1 \
	LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}

%{__mv} $RPM_BUILD_ROOT%{_localedir}/ta_IN $RPM_BUILD_ROOT%{_localedir}/ta
%{__mv} $RPM_BUILD_ROOT%{_localedir}/uk_UA $RPM_BUILD_ROOT%{_localedir}/uk

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc LICENSE README config.txt
%attr(755,root,root) %{_bindir}/zathura
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/zathura.1*
%{_mandir}/man5/zathurarc.5*
%dir %{_libdir}/zathura

%files devel
%defattr(644,root,root,755)
%{_includedir}/zathura
%{_pkgconfigdir}/zathura.pc
