%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	Net_LDAP2
Summary:	%{_pearname} - Object oriented interface for searching and manipulating LDAP-entries
Summary(pl.UTF-8):	%{_pearname} - zorientowany obiektowo interfejs do wyszukiwania i obróbki wpisów LDAP
Name:		php-pear-%{_pearname}
Version:	2.2.0
Release:	1
License:	LGPL License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	70b4b7b033d180d148a53734af073aa6
URL:		http://pear.php.net/package/Net_LDAP2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(ldap)
Requires:	php-pear
Obsoletes:	php-pear-Net_LDAP2-tests
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

%prep
%pear_package_setup

mv docs/%{_pearname}/doc/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_examplesdir}/%{name}-%{version}}
%pear_package_install

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/Net_LDAP2/doc
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/LDAP2.php
%{php_pear_dir}/Net/LDAP2

%{_examplesdir}/%{name}-%{version}
