Summary:	AVI && MPEG to DivX AVI converter
Summary(pl):	Konwerter AVI && MPEG do DivX AVI
Name:		x2divx
Version:	0.4
Release:	1
Group:		X11/Applications/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
License:	GPL
Source0:	http://www.emulinks.de/divx/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
URL:		http://www.emulinks.de/divx/
BuildRequires:	avifile-devel >= 0.50
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for converting AVI and MPEG to DivX encoded AVIs.

%description -l pl
Narzêdzie do konwertowania plików AVI i MPEG do AVI kompresowanych DivXem.

%prep
%setup  -q
%patch0 -p1

%build
OPT="$RPM_OPT_FLAGS" %{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
%{__make} DESTDIR=$RPM_BUILD_ROOT%{_bindir} install                                                                 

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc README.gz
