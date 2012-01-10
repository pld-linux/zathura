Summary:	A vi-like pdf reader
Summary(hu.UTF-8):	Egy vi-szerű pdf olvasó
Summary(pl.UTF-8):	Czytnik pdf podobny do vi
Name:		zathura
Version:	0.0.8.5
Release:	1
License:	BSD-like
Group:		Applications
Source0:	https://pwmt.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	52e0c3b3917c7feaecba98cff8435b90
Source1:	config.txt
URL:		http://pwmt.org/projects/zathura
BuildRequires:	cairo-devel
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel
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

%prep
%setup -q
cp %{SOURCE1} config.txt

%build
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README config.txt
%attr(755,root,root) %{_bindir}/zathura
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/zathura.1*
%{_mandir}/man5/zathurarc.5*
