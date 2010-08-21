%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	JpegMarkerReader
%define		_status		beta
%define		_pearname	Image_JpegMarkerReader
Summary:	%{_pearname} - read arbitrary markers from JPEG files
Summary(pl.UTF-8):	%{_pearname} - odczyt dowolnych znaczników z plików JPEG
Name:		php-pear-%{_pearname}
Version:	0.5.0
Release:	2
License:	MIT License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6dadc6eec1d61499f0f4a2e06a381206
URL:		http://pear.php.net/package/Image_JpegMarkerReader/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR >= 1.4.0b1
Requires:	php-pear-XML_Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows you to easily fetch any particular marker from a
JPEG file. It is primarily a foundation for higher-level packages such
as the JpegXmpReader package.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten pozwala na odczytanie w wygodny sposób poszczególnych
znaczników z pliku JPEG. Jest to klasa bazowa dla pakietów takich jak
Image_JpegXmpReader.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Image/JpegMarkerReader.php
