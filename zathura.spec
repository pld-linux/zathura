#
# Conditional build:
%bcond_with	synctex		# SynxTeX support

%define		_zathura_plugin_api	6
%define		_zathura_plugin_abi	7

Summary:	A vi-like PDF reader
Summary(hu.UTF-8):	Egy vi-szerű PDF olvasó
Summary(pl.UTF-8):	Czytnik PDF podobny do vi
Name:		zathura
Version:	0.5.12
Release:	1
License:	BSD-like
Group:		Applications/Text
Source0:	https://pwmt.org/projects/zathura/download/%{name}-%{version}.tar.xz
# Source0-md5:	c3ad6f2728607b17056be8b98d6d23a4
Source1:	config.txt
URL:		http://pwmt.org/projects/zathura
BuildRequires:	cairo-devel
# C17
BuildRequires:	gcc >= 6:8.1
BuildRequires:	gettext-tools
BuildRequires:	girara-devel >= 0.4.5
BuildRequires:	glib2-devel >= 1:2.76
BuildRequires:	gtk+3-devel >= 3.24
BuildRequires:	intltool
BuildRequires:	json-glib-devel
BuildRequires:	libmagic-devel
# rsvg-convert for png icons
BuildRequires:	librsvg
BuildRequires:	libseccomp-devel >= 2.5.5
BuildRequires:	linux-libc-headers >= 7:6.6.0
BuildRequires:	meson >= 1
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	python-docutils
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	sphinx-pdg
BuildRequires:	sqlite3-devel >= 3.6.23
%{?with_synctex:BuildRequires:	synctex-devel >= 2}
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	girara >= 0.4.5
Requires:	glib2 >= 1:2.76
Requires:	gtk+3 >= 3.24
Requires:	hicolor-icon-theme
Requires:	libseccomp >= 2.5.5
Requires:	sqlite3-libs >= 3.6.23
%{?with_synctex:Requires:	synctex >= 2}
Provides:	zathura(plugin-api) = %_zathura_plugin_api
Provides:	zathura(plugin-abi) = %_zathura_plugin_abi
Suggests:	zathura-pdf-poppler
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define fishdir %{_datadir}/fish/vendor_completions.d

%description
zathura is a highly customizable and functional PDF viewer based on
the poppler rendering library and the GTK+ toolkit. The idea behind
zathura is an application that provides a minimalistic and space
saving interface as well as an easy usage that mainly focuses on
keyboard interaction.

%description -l hu.UTF-8
zathura egy magas szinten konfigurálható és funkcionális PDF olvasó a
poppler és GTK+ könyvtárako alapulva. A zathura célja, hogy egy olyan
alkalmazás legyen, amely minimalista és terület-takarékos felületet
biztosítson, amennyire lehet, és könnyen lehessen használni, főleg
billentyűzet segítségével.

%description -l pl.UTF-8
zathura jest wysoko konfigurowalnym i funkcjonalnym czytnikiem PDF
opartym na bibliotece renderującej poppler i zestawie narzędziowym
GTK+. zathura jest aplikacją, która udostępnia minimalistyczny i nie
zajmujący dużo miejsca interfejs, który jednocześnie jest prosty w
użyciu. Interfejs skupia się głównie na interakcji klawiaturowej.

%package devel
Summary:	Header files for zathura
Summary(pl.UTF-8):	Pliki nagłówkowe aplikacji zathura
Group:		Development/Libraries
# doesn't require base
Requires:	girara-devel >= 0.4.5

%description devel
Header files for zathura.

%description devel -l pl.UTF-8
Pliki nagłówkowe aplikacji zathura.

%package -n bash-completion-zathura
Summary:	Bash completion for zathura command line
Summary(pl.UTF-8):	Bashowe dopełnianie linii poleceń programu zathura
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 1:2.0
BuildArch:	noarch

%description -n bash-completion-zathura
Bash completion for zathura command line.

%description -n bash-completion-zathura -l pl.UTF-8
Bashowe dopełnianie linii poleceń programu zathura.

%package -n fish-completion-zathura
Summary:	fish-completion for zathura
Summary(pl.UTF-8):	Uzupełnianie nazw w fish dla zathura
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	fish
BuildArch:	noarch

%description -n fish-completion-zathura
fish-completion for zathura.

%description -n fish-completion-zathura -l pl.UTF-8
Pakiet ten dostarcza uzupełnianie nazw w fish dla zathura.

%package -n zsh-completion-zathura
Summary:	ZSH completion for zathura command line
Summary(pl.UTF-8):	Dopełnianie linii poleceń programu zathura dla powłoki ZSH
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	zsh
BuildArch:	noarch

%description -n zsh-completion-zathura
ZSH completion for zathura command line.

%description -n zsh-completion-zathura -l pl.UTF-8
Dopełnianie linii poleceń programu zathura dla powłoki ZSH.

%prep
%setup -q
cp %{SOURCE1} config.txt

PLUGIN_API=`sed -n -e '/^plugin_api_version[[:space:]]*=/ s/[^0-9]*\([0-9]*\).*/\1/ p' meson.build`
PLUGIN_ABI=`sed -n -e '/^plugin_abi_version[[:space:]]*=/ s/[^0-9]*\([0-9]*\).*/\1/ p' meson.build`
if [ "$PLUGIN_API" != "%_zathura_plugin_api" ] || [ "$PLUGIN_ABI" != "%_zathura_plugin_abi" ]; then
	if [ "$PLUGIN_API" != "%_zathura_plugin_api" ]; then
		echo "Set %%_zathura_plugin_api to $PLUGIN_API and rerun."
	fi
	if [ "$PLUGIN_ABI" != "%_zathura_plugin_abi" ]; then
		echo "Set %%_zathura_plugin_abi to $PLUGIN_ABI and rerun."
	fi
	exit 1
fi

%build
%meson \
	-Dconvert-icon=enabled \
	-Dlandlock=enabled \
	-Dmanpages=enabled \
	-Dseccomp=enabled \
	-Dsynctex=%{__enabled_disabled synctex} \
	-Dtests=disabled

%meson_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}

%meson_install

%{__mv} $RPM_BUILD_ROOT%{_localedir}/id_ID $RPM_BUILD_ROOT%{_localedir}/id
%{__mv} $RPM_BUILD_ROOT%{_localedir}/no $RPM_BUILD_ROOT%{_localedir}/nb
%{__mv} $RPM_BUILD_ROOT%{_localedir}/ta_IN $RPM_BUILD_ROOT%{_localedir}/ta
%{__mv} $RPM_BUILD_ROOT%{_localedir}/uk_UA $RPM_BUILD_ROOT%{_localedir}/uk

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database_post

%postun
%update_icon_cache hicolor
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc LICENSE README.md config.txt
%attr(755,root,root) %{_bindir}/zathura
%attr(755,root,root) %{_bindir}/zathura-sandbox
%{_desktopdir}/org.pwmt.zathura.desktop
%{_datadir}/metainfo/org.pwmt.zathura.appdata.xml
%{_datadir}/dbus-1/interfaces/org.pwmt.zathura.xml
%{_iconsdir}/hicolor/*x*/apps/org.pwmt.zathura.png
%{_iconsdir}/hicolor/scalable/apps/org.pwmt.zathura.svg
%{_mandir}/man1/zathura.1*
%{_mandir}/man1/zathura-sandbox.1*
%{_mandir}/man5/zathurarc.5*
%dir %{_libdir}/zathura

%files devel
%defattr(644,root,root,755)
%{_includedir}/zathura
%{_pkgconfigdir}/zathura.pc

%files -n bash-completion-zathura
%defattr(644,root,root,755)
%{bash_compdir}/zathura

%files -n fish-completion-zathura
%defattr(644,root,root,755)
%{fishdir}/zathura.fish

%files -n zsh-completion-zathura
%defattr(644,root,root,755)
%{zsh_compdir}/_zathura
