Summary:	A vi-like pdf reader
Name:		zathura
Version:	0.0.8.1
Release:	1
License:	BSD-like
Group:		Applications
Source0:	http://pwmt.org/attachments/download/10/%{name}-%{version}.tar.gz
# Source0-md5:	67351e5ab66cfdda9a71c9ce6c47a970
URL:		http://pwmt.org/projects/zathura
BuildRequires:	cairo-devel
BuildRequires:	glib-devel
BuildRequires:	gtk+2-devel
BuildRequires:	poppler-glib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zathura is a highly customizable and functional PDF viewer based on
the poppler rendering library and the gtk+ toolkit. The idea behind
zathura is an application that provides a minimalistic and space
saving interface as well as an easy usage that mainly focuses on
keyboard interaction.

%prep
%setup -q

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
%doc LICENSE README
%attr(755,root,root) %{_bindir}/zathura
%{_mandir}/man1/zathura.1*
