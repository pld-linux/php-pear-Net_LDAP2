%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	LDAP2
%define		_status		beta
%define		_pearname	Net_LDAP2

Summary:	%{_pearname} - Object oriented interface for searching and manipulating LDAP-entries
Summary(pl.UTF-8):	%{_pearname} - zorientowany obiektowo interfejs do wyszukiwania i obróbki wpisów LDAP
Name:		php-pear-%{_pearname}
Version:	2.0.0
Release:	0.RC2.1
License:	LGPL License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}RC2.tgz
# Source0-md5:	78a7492dda5f67a21bd3857f9c5d3171
Patch0:		%{name}-paths.patch
URL:		http://pear.php.net/package/Net_LDAP2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_LDAP2 is the successor of Net_LDAP which is a clone of Perls
Net::LDAP object interface to directory servers. It does contain most
of Net::LDAPs features but has some own too.

With Net_LDAP2 you have:
 - A simple object-oriented interface to connections, searches entries
   and filters,
 - Support for TLS and LDAP v3,
 - Simple modification, deletion and creation of LDAP entries,
 - Support for schema handling,
 - Net_LDAP2 layers itself on top of PHP's existing LDAP extensions.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Net_LDAP2 to następca Net_LDAP, klonu Perlowego obiektowego interfejsu
NET::LDAP do serwerów katalogowych. Pakiet ten zawiera większość
funkcjonalności Net::LDAP jak również trochę dodatkowej.

Cechy Net_LDAP2:
 - prosty, zorientowany obiektowo interfejs do połączeń, wyszukiwania i
   filtrowania,
 - wsparcie dla TLS i LDAP v3,
 - wygodny sposób na modyfikację usuwanie i tworzenie wpisów LDAP,
 - wsparcie dla obsługi schematów,
 - NET_LDAP2 wykorzystuje istniejące rozszerzenie LDAP.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/Net_LDAP2/doc
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/LDAP2
%{php_pear_dir}/Net/LDAP2.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Net_LDAP2
