Summary:	DevHelp book: atk
Summary(pl):	Ksi±¿ka do DevHelpa o atk
Name:		devhelp-book-atk
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/atk.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
DevHelp book about atk.

%description -l pl
Ksi±¿ka do DevHelpa o atk.

%prep
%setup -q -c -n atk

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/atk,specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/atk.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/atk

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
