%define up_name CamlGI
%define name	ocaml-camlgi
%define version	0.6
%define release	%mkrel 1
%define ocaml_sitelib %(if [ -x /usr/bin/ocamlc ]; then ocamlc -where;fi)/site-lib

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl compatibility regular expressions for OCaml
Source: 	http://downloads.sourceforge.net/ocaml-cgi/%{up_name}-%{version}.tar.bz2
URL:		http://sourceforge.net/projects/ocaml-cgi/
License:	GPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRequires:	camlp4
BuildRequires:  findlib
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
CamlGI is a library to enable you to write CGI and FastCGI in OCaml. It is
written 100% in OCaml so should run on many platforms. The library supports
multiple simultaneous connections and request multiplexing while presenting an
easy to use interface.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n %{up_name}-%{version}

%build
%make

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{ocaml_sitelib}
make install OCAMLFIND_DESTDIR="-destdir %{buildroot}/%{ocaml_sitelib}"

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc LICENSE README
%{ocaml_sitelib}/CamlGI


