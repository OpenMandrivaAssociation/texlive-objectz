# revision 19389
# category Package
# catalog-ctan /macros/latex/contrib/objectz
# catalog-date 2006-12-30 22:14:40 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-objectz
Version:	20180303
Release:	1
Summary:	Macros for typesetting Object Z
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/objectz
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/objectz.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/objectz.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/objectz.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package will typeset both Z and Object-Z specifications; it
develops the original zed package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/objectz/oz.sty
%doc %{_texmfdistdir}/doc/latex/objectz/catalog
%doc %{_texmfdistdir}/doc/latex/objectz/makefile
%doc %{_texmfdistdir}/doc/latex/objectz/manifest
%doc %{_texmfdistdir}/doc/latex/objectz/ozguide.pdf
%doc %{_texmfdistdir}/doc/latex/objectz/ozguide.tex
%doc %{_texmfdistdir}/doc/latex/objectz/oztest.tex
%doc %{_texmfdistdir}/doc/latex/objectz/readme
#- source
%doc %{_texmfdistdir}/source/latex/objectz/oz.dtx
%doc %{_texmfdistdir}/source/latex/objectz/oz.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061230-2
+ Revision: 754464
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061230-1
+ Revision: 719147
- texlive-objectz
- texlive-objectz
- texlive-objectz
- texlive-objectz

